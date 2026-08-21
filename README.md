# IDS-JODHA

### Indian Driving Scenes – Jodhpur Dataset for Heterogeneous Environment Analysis

<p align="center">
  <strong>A real-world multimodal and multi-weather traffic dataset for studying heterogeneous agents and unstructured driving environments.</strong>
</p>

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.17258045">
    <img src="https://zenodo.org/badge/DOI/10.5281/zenodo.17258045.svg" alt="Dataset DOI">
  </a>
  <a href="https://shaaashvat.github.io/ids-jodha/">
    <img src="https://img.shields.io/badge/Project-Website-blue" alt="Project Website">
  </a>
  <a href="https://github.com/palsreejib/JODHA">
    <img src="https://img.shields.io/badge/Code-GitHub-black?logo=github" alt="GitHub Repository">
  </a>
</p>

---

## Overview

**IDS-JODHA** is a real-world multimodal and multi-weather traffic dataset collected on urban roads in **Jodhpur, Rajasthan, India**.

The dataset captures heterogeneous and relatively unstructured traffic environments involving diverse road users, including vehicles and pedestrians. It combines high-resolution camera observations with 3D LiDAR measurements to provide synchronized multimodal representations of the driving scene.

The dataset contains observations under both **clear-weather** and **rainy-weather** conditions, enabling the study of traffic dynamics and perception across different environmental conditions.

IDS-JODHA is intended to support research in areas including:

- Autonomous driving and ADAS
- Multimodal perception
- 3D LiDAR-based perception
- Traffic behavior and agent dynamics
- Heterogeneous traffic analysis
- Multi-weather perception
- Complex systems and traffic-flow analysis

---

## Dataset at a Glance

| Property | Details |
|:--|:--|
| **Location** | Jodhpur, Rajasthan, India |
| **Environment** | Urban, heterogeneous traffic |
| **Modalities** | Camera + 3D LiDAR |
| **Video frames** | 87,000+ |
| **LiDAR scans** | 16,000+ synchronized scans |
| **Camera** | Sony ILCE-6400 |
| **Camera resolution** | 3840 × 2160 |
| **LiDAR** | Velodyne Puck VLP-16 |
| **LiDAR channels** | 16 |
| **LiDAR frequency** | 10 Hz |
| **Weather conditions** | Clear + rainy |
| **Dataset size** | 176.1 GB |

---

## Project Resources

| Resource | Link |
|:--|:--|
| **Dataset** | [Zenodo](https://doi.org/10.5281/zenodo.17258045) |
| **Project Website** | [IDS-JODHA Website](https://shaaashvat.github.io/ids-jodha/) |
| **Source Code** | [GitHub](https://github.com/palsreejib/JODHA) |
| **Publication** | *Coming soon / see project website* |

> **Note:** The complete dataset is hosted on Zenodo. This repository contains the project code, ROS 2 acquisition package, and documentation.

---

## Repository Overview

This repository contains the ROS 2 acquisition code used for the LiDAR data collection pipeline, together with the documentation required to understand and reproduce the acquisition setup.

The core custom ROS 2 package is located at:

```text
ros2_ws/src/velodyne_bringup/
