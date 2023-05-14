![20230512_161300](https://github.com/s5y-ux/Hands_To_OLED/assets/59636597/c82f5acc-ffdb-4fed-bc15-5c2ec9208bdf)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
# Hands To OLED
Hands to OLED is a project that leverages the power of Mediapipe, an open-source framework for building multimodal (audio, video, and sensor) applied ML pipelines, to track the position of a pointer finger in real-time. By utilizing the Mediapipe hand tracking solution, the project extracts the x and y coordinates of the finger and communicates this data to an OLED display via a serial monitor encoding scheme. This allows users to visualize and interact with the tracked finger position so the data may be used for logical operations in integrated circuits

## Mediapipe

MediaPipe is an open-source framework developed by Google that provides a flexible platform for building real-time multimedia processing pipelines. It enables developers to create applications that can analyze and manipulate video and audio streams, making it ideal for a wide range of applications such as augmented reality, gesture recognition, facial detection, and more. MediaPipe is designed to be cross-platform and supports various operating systems, including Android, iOS, Linux, and Windows.

At its core, MediaPipe offers a graph-based data processing framework. The processing pipeline is represented as a directed acyclic graph (DAG), where nodes in the graph represent processing components, and edges define the data flow between these components. Each node performs a specific task, such as image or video processing, feature extraction, machine learning inference, or rendering.

MediaPipe provides a rich set of pre-built components that developers can use to construct their pipelines. These components, known as calculators, encapsulate various algorithms and functionality, allowing developers to easily assemble complex pipelines without having to implement everything from scratch. Additionally, developers can also create their own custom calculators to incorporate specific functionality or tailor the pipeline to their requirements.

One of the key features of MediaPipe is its support for real-time processing on mobile and embedded devices. It leverages hardware acceleration and optimizations to achieve efficient execution and low latency, making it suitable for applications that require real-time feedback or interactive experiences. MediaPipe utilizes the underlying hardware capabilities, such as GPUs or specialized processors, to maximize performance and ensure smooth operation even on resource-constrained devices.
<img width="1073" alt="hand-landmarks" src="https://github.com/s5y-ux/Hands_To_OLED/assets/59636597/48680f99-976f-4b2e-80fc-ee236e5d4e4c">

## Adafruit's GFX Library

The "Adafruit_GFX.h" library is a C++ graphics library provided by Adafruit Industries. It is designed to work in conjunction with display-specific libraries, such as the "Adafruit_SSD1306.h" library, to provide a set of graphics functions for drawing shapes, text, and images on displays.

The "Adafruit_GFX.h" library provides a common set of graphics functions that are independent of the underlying display hardware. It includes functions for drawing basic shapes like lines, rectangles, circles, triangles, and rounded rectangles. Additionally, it supports font rendering for displaying text in different sizes and styles. The library also includes functions for manipulating pixels, colors, and performing basic transformations on graphical objects.

## Adafruit's SSD1306 Library

The "Adafruit_SSD1306.h" library is a C++ library provided by Adafruit Industries. It is specifically designed to interface with SSD1306-based OLED displays, which are commonly used in various electronic projects. This library simplifies the task of controlling and displaying content on these OLED displays.

The SSD1306 is a popular display controller chip that supports monochrome OLED displays with different resolutions, such as 128x64 pixels or 128x32 pixels. The Adafruit_SSD1306 library abstracts the low-level details of communicating with the SSD1306 chip and provides a high-level interface to easily control the display.

## Video

https://github.com/s5y-ux/Hands_To_OLED/assets/59636597/f75a68c2-ae85-46ad-8f16-ca1bc5a2f2ea
