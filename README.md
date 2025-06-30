# Ecosight Technologies - Python Fullstack Assignment

## Overview

This application is a full-stack solution that utilizes the StarVector model to convert user-uploaded images into SVG code. The application exposes a GraphQL API to handle image submissions and retrieval of SVG results and provides a React-based frontend for user interaction.

## Features

- **Image-to-SVG Conversion:** Utilizes the StarVector model to process raster images (e.g., PNG, JPEG) and generate corresponding SVG code.
- **GraphQL API:** Implements a GraphQL API using FastAPI and Strawberry for handling image uploads and retrieval of SVG results.
- **React Frontend:** Provides a user-friendly interface for uploading images and viewing the generated SVG output.
- **Docker Support:** Includes Dockerfiles and a Docker Compose configuration for easy deployment and development setup.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/downloads/) (3.7 or later)
- [Node.js](https://nodejs.org/) (for frontend development)

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd ecosight_app
