![20230512_161300](https://github.com/s5y-ux/Hands_To_OLED/assets/59636597/c82f5acc-ffdb-4fed-bc15-5c2ec9208bdf)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# Hands To OLED
Hands to OLED is a project that leverages the power of Mediapipe, an open-source framework for building multimodal (audio, video, and sensor) applied ML pipelines, to track the position of a pointer finger in real-time. By utilizing the Mediapipe hand tracking solution, the project extracts the x and y coordinates of the finger and communicates this data to an OLED display via a serial monitor encoding scheme. This allows users to visualize and interact with the tracked finger position in a tangible and intuitive manner.

## Mediapipe

MediaPipe is an open-source framework developed by Google that provides a flexible platform for building real-time multimedia processing pipelines. It enables developers to create applications that can analyze and manipulate video and audio streams, making it ideal for a wide range of applications such as augmented reality, gesture recognition, facial detection, and more. MediaPipe is designed to be cross-platform and supports various operating systems, including Android, iOS, Linux, and Windows.

At its core, MediaPipe offers a graph-based data processing framework. The processing pipeline is represented as a directed acyclic graph (DAG), where nodes in the graph represent processing components, and edges define the data flow between these components. Each node performs a specific task, such as image or video processing, feature extraction, machine learning inference, or rendering.

MediaPipe provides a rich set of pre-built components that developers can use to construct their pipelines. These components, known as calculators, encapsulate various algorithms and functionality, allowing developers to easily assemble complex pipelines without having to implement everything from scratch. Additionally, developers can also create their own custom calculators to incorporate specific functionality or tailor the pipeline to their requirements.

One of the key features of MediaPipe is its support for real-time processing on mobile and embedded devices. It leverages hardware acceleration and optimizations to achieve efficient execution and low latency, making it suitable for applications that require real-time feedback or interactive experiences. MediaPipe utilizes the underlying hardware capabilities, such as GPUs or specialized processors, to maximize performance and ensure smooth operation even on resource-constrained devices.
<img width="1073" alt="hand-landmarks" src="https://github.com/s5y-ux/Hands_To_OLED/assets/59636597/48680f99-976f-4b2e-80fc-ee236e5d4e4c">
