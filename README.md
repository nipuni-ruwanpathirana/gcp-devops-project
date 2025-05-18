# 🌐 GCP DevOps Project – CI/CD Pipeline with Docker, Cloud Build, and GKE

This project demonstrates a complete DevOps pipeline for deploying a simple Python Flask web application on **Google Cloud Platform (GCP)** using **Docker**, **Cloud Build**, and **Google Kubernetes Engine (GKE)**. It follows modern CI/CD practices and infrastructure automation techniques.

---

## 🚀 Project Overview

- **App**: A basic Python Flask app.
- **CI/CD**: Implemented using Google Cloud Build to automate Docker image builds and GKE deployments.
- **Containerization**: The app is containerized using Docker.
- **Deployment**: Deployed to a GKE cluster in the `asia-south1-a` region with a LoadBalancer service for external access.
- **Infrastructure**: Configured with Kubernetes manifests and a Cloud Build YAML file for seamless integration.

---

## 🔧 Tech Stack

- **Python 3.12 (Flask)**
- **Docker**
- **Google Cloud Build**
- **Google Kubernetes Engine (GKE)**
- **Kubernetes YAML (Deployment & Service)**

---

## 📦 How It Works

- **Docker Build**: Cloud Build builds the Docker image for the app.
- **Docker Push**: The image is pushed to Artifact Registry (`gcr.io`).
- **GKE Deploy**: Using `gke-deploy`, the image is deployed to the GKE cluster using `gke.yaml`.
- **Load Balancer**: A Kubernetes LoadBalancer service exposes the app to the internet on port 80.

---

## 📌 Key Features

- End-to-end DevOps pipeline with CI/CD automation.
- Docker-based containerization and GKE orchestration.
- Clean separation of build, deploy, and infrastructure steps.
- Follows best practices for cloud-native app deployment.
