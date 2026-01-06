# An In-Depth Analysis of Query Optimization Techniques in Modern DBMS

## Abstract
This repository contains the data synthesis and visualization artifacts for the research paper "An In-Depth Analysis of Query Optimization Techniques in Modern Database Management Systems." [cite_start]The study presents a comparative analysis of rule-based, cost-based, adaptive, and machine learning-based approaches, evaluating them on query latency, resource utilization, and scalability[cite: 15, 17].

## Authors
* **Ng Huey Xuan** (Analysis of Results & Discussion)
* **Cheng Qin He Niczen** (Results & Conclusion)
* **How Pei Yan** (Introduction & Literature Review)
* *School of Engineering and Technology, Sunway University* 

## Project Overview
This project supports the findings that:
1. **Cost-based optimization** remains the standard for structured relational workloads but struggles with data skew.
2. **Adaptive and ML-based techniques** offer superior scalability and latency reduction in distributed environments but incur high system overhead.

## Repository Contents
* **/data**: Structured datasets extracted from the Systematic Literature Review (SLR).
* **/notebooks**: Python scripts used to generate the comparative graphs (Figures 2, 5, and 6 in the paper).
* **/results**: Visual evidence supporting the trade-off analysis between performance and system complexity.

## Key Findings Supported
| Optimization Technique | Avg Latency (ms) | Scalability | System Overhead |
|------------------------|------------------|-------------|-----------------|
| Rule-Based             | ~200             | Low         | Very Low        |
| Cost-Based             | ~110             | Medium      | Medium          |
| Adaptive               | ~90              | High        | Medium-High     |
| ML-Based               | ~70              | Very High   | High            |
*(Data derived from Table VI and Fig 2 in the paper)*
