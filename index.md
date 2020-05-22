---
layout: splash
title: "A Face in the Crowd: A Contextualized, Integrated, Intro to Linear Algebra"
header:
  overlay_color: "#419AD9"
  overlay_filter: "0.0"
  overlay_image: website_graphics/olin_logo.jpg
feature_row:
  - image_path: https://img.youtube.com/vi/MFL4gd2IMm8/0.jpg
    alt: "A thumbnail image for a video.  The text QEA Olin College of Engineering appears on a textured blue background"
    title: "Key Features of QEA"
    excerpt: "QEA is a highly interdisciplinary, integrated course for teaching technical content."
    url: "#course-philosophy"
    btn_label: "More details about QEA"
    btn_class: "btn--primary"
  - image_path: website_graphics/faces_collage.png
    alt: "A 5 by 5 grid of face images with labels of whether each of them are smiling."
    title: "Computational Platform"
    excerpt: "Students use MATLAB as a programming environment during this module.  Use the button below to see sample code and other supporting materials."
    url: "#supporting-resources"
    btn_label: "Supporting Resources"
    btn_class: "btn--primary"
  - image_path: website_graphics/eigface1_stretched.jpg
    alt: "A sample Eigenface calculated from the class dataset."
    title: "Module Overview"
    excerpt: "The module introduces fundamental ideas in linear algebra through a deep dive into creating a facial recognition system."
    url: "#module-details"
    btn_label: "Module Details"
    btn_class: "btn--primary"

feature_row_computational_platform:
  - image_path: website_graphics/faces_collage.png
    alt: "A 5 by 5 grid of face images with labels of whether each of them are smiling."
    excerpt: "These resources provide some of the sample code we give in an easy to download and view format along with a guide to setting up your own photo booth so one can collect a dataset of images for facial recognition from a class.\n

    ### Sample MATLAB Code\n
    * [Sample Code](Sample_code/sample_code)\n

    ### Teaching Team Documentation\n
    * [How to run the Photo Booth](How to/photo_booth)"

feature_row_linalg_basics:
  - image_path: website_graphics/RGBArrayWithSlice.png
    alt: "A schematic of the representation of a red, green, and blue image as a matrix"
    excerpt: "
   The module begins with a day 1 activity that frames the big ideas of facial recognition (both in terms of technical concepts and societal implications).  Students then build their understanding of the basic entities of linear algebra and how to operate on them.\n

    ### Schedule and Supporting Documents

* [Day 1: Facial Recognition: The Big Picture](Chapters/M1_Day1.pdf)\n
* [Night 1: Introduction to Matrices](Chapters/M1_Night1.pdf)\n
* [Day 2: Matrix Transformations](Chapters/M1_Day2.pdf)\n 
* [Night 2: Matrix Operations](Chapters/M1_Night2.pdf)\n 
* [Day 3: Linear Independence, Span, Basis, and Decomposition](Chapters/M1_Day3.pdf)\n 
* [Night 3: Linear Systems of Algebraic Equations](Chapters/M1_Night3.pdf)\n"

feature_row_eigenthings_and_applications_of_linalg:
  - image_path: website_graphics/covariancedirections.png
    alt: "A 3D scatter plot showing the relationship between the temperature in 3 cities along with the principal directions of variance shown as vectos."
    excerpt: "Next, students take the basic properties of matrices and vectors they have learned and learn key concepts of Eigenvalues and Eigenvectors.  Our presentation of these important concepts is heavy on visualization and intuition-building.  We also provide several compelling applications of these concepts to help students understand the power and utility of the theory they are learning.

    ### Schedule and Supporting Documents

* [Day 4: Linear Systems of Algebraic Equations](Chapters/M1_Day4.pdf)\n 
* [Night 4: Facial Recognition, Image Manipulation and Decomposition](Chapters/M1_Night4.pdf)\n 
* [Day 5: Linear Systems of Algebraic Equations, Brain data, and Context and Ethics](Chapters/M1_Day5.pdf)\n 
* [Night 5: Correlation](Chapters/M1_Night5.pdf)\n 
* [Day 6: AI Discussion, Smile Detection and Eigenthings](Chapters/M1_Day6.pdf)\n 
* [Night 6: Eigenvalues and Eigenvectors](Chapters/M1_Night6.pdf)" 

feature_matrix_decomposition_and_project:
  - image_path: website_graphics/eigface1.jpg
    alt: "An image of an Eigenface computed using principal components analysis"
    excerpt: "Students learn about several algorithms for matrix decomposition: Eigenvalue Decomposition, Singular Value Decomposition, and Principal Components Analysis. The module culminates with a substantial project in which students build algorithms for facial recognition and processing while seriously considering the implications of their work for potential users and society in general.

    ### Schedule and Supporting Documents

* [Day 7: Eigenvalue Decomposition and Principal Components Analysis](Chapters/M1_Day7.pdf)\n 
* [Night 7: Principal Components Analysis and Eigenfaces](Chapters/M1_Night7.pdf)\n 
* [Day 8: Eigenface Synthesis and Project Kick-Off](Chapters/M1_Day8.pdf)\n 
* [Night 8: Eigenfaces Paper and Project Ideation](Chapters/M1_Night8.pdf)\n 
* [Day 9: Project Kickoff](Chapters/M1_Day9.pdf)\n
* [Project: The Context and Consequences of Feature Recognition,
Detection, and Classification](Chapters/M1_Project.pdf)" 
---

The module "A Face in the Crowd" is the opening module in the 12-credit, 3-semester QEA sequence.  The module introduces the major ideas in linear algebra with a focus on intuition building and application in an effort to build deep understanding.  The module is organized around the engineering challenging of building a facial recognition systems.  Rather than purely focus on the technical components of this challenge, students read about the societal issues surrounding the technology (e.g., algorithmic bias).  Along the way students also see applications of linear algebra applied to different domains (e.g., neuroscience).

The full course "textbook" can be found using this link [AFaceInTheCrowdSpring2020.pdf](FullBookAndSourceLatex/AFaceInTheCrowdSpring2020.pdf).  Source files for this website and the assignments themselves can be found at [https://github.com/qeacourse/AFaceInTheCrowd](https://github.com/qeacourse/AFaceInTheCrowd).

{% include feature_row %}

*Inspired to learn more?  E-mail <a href="mailto:Collaboratory@olin.edu">Collaboratory@olin.edu</a>.*


## <a name="course-philosophy"/> QEA in a Nutshell

Quantitative Engineering Analysis (QEA) is an interdisciplinary, integrated, course for students to become proficient in learning new technical content and successfully completing projects that have a significant analytical component to them.  This video summarizes some of the rationale and specific pedagogy behind the course.

<p align="center">
 <iframe src="https://www.youtube.com/embed/MFL4gd2IMm8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

## <a name="supporting-resources"/> Supporting Documentation and Code

{% include feature_row id="feature_row_computational_platform" type="left" %}

## <a name="module-details"/> Big Picture Framing and Linear Algebra Basics

{% include feature_row id="feature_row_linalg_basics" type="right" %}

## Eigenthings and Applications of Linear Algebra

{% include feature_row id="feature_row_eigenthings_and_applications_of_linalg" type="left" %}

## Matrix Decomposition with Applications in a Project

{% include feature_row id="feature_matrix_decomposition_and_project" type="right" %}

## Conclusion and Learning More

The module "A Face in the Crowd" is a deep dive into the linear algebra and its myriad applications.  The module builds towards the creation of algorithms for face processing and recognition, but along the way many other applications of the powerful ideas in linear algebra are shown.  We have found that this approach to teaching linear algebra gives a high degree of intuition and understanding of the most important concepts while keeping "turning the crank" (e.g., doing Gaussian elimination by hand) to a minimum.

### Other Documents on QEA

* S. Govindasamy, R.J. Christianson, J. Geddes, C. Lee, S. Michalka, P. Ruvolo, M.H. Somerville, A.C. Strong: [A Contextualized, Experiential Learning Approach to Quantitative Engineering Analysis](https://ieeexplore.ieee.org/document/8658526), FIE 2018.
