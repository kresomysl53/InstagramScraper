# 📸 Instagram Profile Scraper

> Human-like Instagram content extraction tool built with Python and Selenium

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](#)

### Currently used for posts only 

## ✨ Features

# 📸 Instagram Profile Scraper
> Human-like Instagram content extractor built with Python and Selenium

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](#)

**Currently supports post extraction only**

## ✨ Features

### Authentication & Session Management
- Cookie-based session persistence for login reuse  
- Human typing simulation with natural delays  
- Secure credential handling  

### Anti-Detection Techniques
- Randomized delays and scroll behavior  
- Non-headless browser mode for stealth  
- Automation flag removal and fingerprint masking  

### Data Extraction
- Duplicate detection to avoid repeated content  
- Progressive scrolling to load posts dynamically  
- Extraction of image URLs from Instagram CDN  
- Structured output for easy post-processing  

## ⚠️ Ethical Usage Notice
- Respects Instagram's terms of service and rate limits  
- Uses natural browsing patterns and authentic browser signatures  
- Designed for research and educational purposes only  

### Timing Parameters & Performance Metrics

The scraper uses triangular distribution for natural request timing:

**Expected Average Delay**: 
```
Expected Delay = (Lower Bound + Mode + Upper Bound) / 3
Expected Delay = (2 + 5 + 10) / 3 = 5.67 seconds
```

**Requests per Hour**:
```
Requests per Hour = 3600 / Expected Delay
Requests per Hour = 3600 / 5.67 ≈ 635 requests/hour
```

**Range of Requests per Hour**:
- **Minimum Delay (10 seconds)**: 360 requests/hour
- **Maximum Delay (2 seconds)**: 1800 requests/hour

### Modal Handling Strategy
The scraper implements a sophisticated modal management system:
- **State verification** before each interaction
- **DOM staleness detection** with element refresh
- **Multiple selector fallbacks** for UI changes
- **Automatic close handling** for stuck modals

### Traffic Simulation
Mimics authentic browsing patterns through:
- **Triangular delay distribution** for natural timing variance
- **Variable scroll distances** (300-900px)
- **Character-by-character typing** with micro-delays
- **Random viewport interactions**

## 📈 Performance Summary

- **Expected Delay**: ~5.67 seconds
- **Expected Requests per Hour**: ~635 requests/hour
- **Range**: 360-1800 requests/hour (depending on delay variance)
- **Success Rate**: >99% with proper session management (got blocked only once from start without session handling)

## ⚠️ Not intended for:**misuse or activities that harm Instagram.

<p align="center">
  <strong>Built on Earth, by Earth 🌍</strong>
</p>
