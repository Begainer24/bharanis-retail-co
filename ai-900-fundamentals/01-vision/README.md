# 01 — Computer Vision (AI-900 Domain: Computer vision workloads, 15-20%)

## What this demos
Using Azure AI Vision to analyze product images for Bharani's Retail & Co.'s synthetic catalog — image tagging, captioning, and basic object detection.

## Exam concepts this covers
- Image classification vs. object detection vs. OCR — what each is for
- Azure AI Vision service capabilities (tagging, captioning, brand detection, moderation)
- How confidence scores work in vision predictions

## What's in this folder
- `vision_tagging.ipynb` — calls Azure AI Vision on a handful of synthetic product photos, prints out tags + confidence scores, and captions each image

## Setup notes
- Needs an Azure AI Vision resource (free tier: F0, 5,000 transactions/month)
- API key and endpoint should go in a `.env` file (never commit this — add `.env` to `.gitignore`)
