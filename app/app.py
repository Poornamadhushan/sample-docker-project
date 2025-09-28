import os
import io
import streamlit as st
from PIL import Image
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()

# Initialize session state for error tracking
if 'env_error' not in st.session_state:
    st.session_state.env_error = False
if 'client_error' not in st.session_state:
    st.session_state.client_error = False

# Check environment variables
try:
    VISION_KEY = os.environ['VISION_KEY']
    VISION_ENDPOINT = os.environ['VISION_ENDPOINT']
    st.session_state.env_error = False
except:
    st.session_state.env_error = True
    VISION_KEY = None
    VISION_ENDPOINT = None

# Try to create client if env vars are available
client = None
if not st.session_state.env_error:
    try:
        client = ComputerVisionClient(
            endpoint=VISION_ENDPOINT,
            credentials=CognitiveServicesCredentials(VISION_KEY)
        )
        st.session_state.client_error = False
    except:
        st.session_state.client_error = True


st.title('Computer Vision with Streamlit')

# Display error messages if there are issues
if st.session_state.env_error:
    st.error("❌ Missing Azure credentials! Please check your .env file contains:")
    st.code("""VISION_KEY=your_azure_vision_api_key
VISION_ENDPOINT=https://your-vision-endpoint.cognitiveservices.azure.com/""")
    st.info("💡 Make sure your .env file is in the same directory as app.py")
    st.stop()

if st.session_state.client_error:
    st.error("❌ Cannot connect to Azure Computer Vision. Please check your credentials.")
    st.stop()

if client is None:
    st.error("❌ Azure Computer Vision client not initialized.")
    st.stop()

uploadedFile = st.file_uploader('Choose image', type=['jpg', 'jpeg'])

if uploadedFile:
    image = Image.open(uploadedFile)
    st.image(image, caption='Uploaded image')

    imageBytes = io.BytesIO()
    image.save(imageBytes, format=image.format)
    imageBytes = imageBytes.getvalue()

    if st.button('Analyze image'):
        try:
            # Convert bytes back to BytesIO stream for Azure API
            image_stream = io.BytesIO(imageBytes)
            
            result = client.analyze_image_in_stream(
                image=image_stream,
                visual_features=['Tags', 'Description', 'Color']
            )

            if len(result.description.captions) > 0:
                st.write("Caption:")
                st.write(f'{result.description.captions[0].text}')
                st.write(f'Confidence: {result.description.captions[0].confidence:.4f}')

            if len(result.tags) > 0:
                st.write('Tags')
                
                # Display tags in columns for better layout
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write("**Tag**")
                    for tag in result.tags[:10]:
                        st.write(f"• {tag.name}")
                
                with col2:
                    st.write("**Confidence**")
                    for tag in result.tags[:10]:
                        st.write(f"{tag.confidence:.4f}")
                
                # Also show as simple list
                st.write("**All Tags:**")
                for i, tag in enumerate(result.tags[:15], 1):
                    st.write(f"{i}. **{tag.name}** - {tag.confidence:.4f}")
        except Exception as e:
            st.error(f'There was an error when analysing the image: {e}')