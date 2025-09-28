# Azure Computer Vision Streamlit App

A Streamlit web application that uses Azure Computer Vision API to analyze uploaded images and extract insights such as descriptions, tags, and color information.

## 🚀 Features

- **Image Upload**: Upload images in JPG/JPEG format
- **Image Analysis**: Analyze images using Azure Computer Vision API
- **Description Generation**: Get AI-generated descriptions of uploaded images
- **Tag Detection**: Extract relevant tags with confidence scores
- **Color Analysis**: Analyze dominant colors in images
- **Docker Support**: Containerized application for easy deployment
- **Error Handling**: Comprehensive error handling and user feedback

## 🛠️ Technologies Used

- **Python 3.10**
- **Streamlit** - Web application framework
- **Azure Computer Vision API** - Image analysis service
- **PIL (Pillow)** - Image processing
- **Docker** - Containerization
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

Before running this application, you need:

1. **Azure Subscription** with Computer Vision resource created
2. **Azure Computer Vision API Key** and **Endpoint URL**
3. **Python 3.10+** (if running locally)
4. **Docker** (if running in container)

## 🔧 Setup Instructions

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Poornamadhushan/sample-docker-project.git
   cd sample-docker-project
   ```

2. **Create environment file**
   Create a `.env` file in the `app` directory with your Azure credentials:
   ```env
   VISION_KEY=your_azure_vision_api_key
   VISION_ENDPOINT=https://your-vision-endpoint.cognitiveservices.azure.com/
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   cd app
   streamlit run app.py
   ```

5. **Access the application**
   Open your browser and go to `http://localhost:8501`

### Docker Setup

1. **Build the Docker image**
   ```bash
   docker build -t azure-vision-app .
   ```

2. **Run the Docker container**
   ```bash
   docker run -p 8501:8501 --env-file app/.env azure-vision-app
   ```

3. **Access the application**
   Open your browser and go to `http://localhost:8501`

## 🌐 Azure Computer Vision Setup

1. **Create Azure Computer Vision Resource**
   - Go to [Azure Portal](https://portal.azure.com)
   - Create a new Computer Vision resource
   - Note down the API Key and Endpoint URL

2. **Configure Environment Variables**
   - Copy your API Key to `VISION_KEY`
   - Copy your Endpoint URL to `VISION_ENDPOINT`

## 📁 Project Structure

```
sample-docker-project/
├── app/
│   ├── app.py              # Main Streamlit application
│   ├── Pipfile             # Pipenv dependencies
│   ├── Pipfile.lock        # Pipenv lock file
│   └── __pycache__/        # Python cache files
├── .streamlit/
│   └── config.toml         # Streamlit configuration
├── Dockerfile              # Docker container configuration
├── Pipfile                 # Root Pipenv file
├── Pipfile.lock           # Root Pipenv lock file
├── requirements.txt        # Python dependencies
├── .dockerignore          # Docker ignore file
├── .gitignore             # Git ignore file
└── README.md              # Project documentation
```

## 📊 Usage

1. **Launch the application** using one of the setup methods above
2. **Upload an image** by clicking "Choose image" and selecting a JPG/JPEG file
3. **Click "Analyze image"** to process the image with Azure Computer Vision
4. **View results** including:
   - AI-generated image description with confidence score
   - Detected tags with confidence scores
   - Color analysis information

## 🐳 Docker Commands

```bash
# Build the image
docker build -t azure-vision-app .

# Run the container
docker run -p 8501:8501 --env-file app/.env azure-vision-app

# Run in detached mode
docker run -d -p 8501:8501 --env-file app/.env azure-vision-app

# Stop all running containers
docker stop $(docker ps -q)

# Remove the image
docker rmi azure-vision-app
```

## 🔍 API Features Used

This application uses the following Azure Computer Vision API features:

- **Description**: Generates human-readable descriptions of images
- **Tags**: Identifies objects, living beings, scenery, and actions
- **Color**: Analyzes dominant colors and color schemes

## ⚠️ Error Handling

The application includes comprehensive error handling for:

- Missing environment variables
- Invalid Azure credentials
- Network connectivity issues
- Image processing errors
- API rate limiting

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Support

If you encounter any issues:

1. Check that your Azure credentials are correctly configured
2. Ensure your Azure Computer Vision resource is active
3. Verify network connectivity to Azure services
4. Check the Streamlit error messages for specific guidance

## 🔗 Useful Links

- [Azure Computer Vision Documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Docker Documentation](https://docs.docker.com/)

---

**Author**: Poornamadhushan  
**Repository**: [sample-docker-project](https://github.com/Poornamadhushan/sample-docker-project)