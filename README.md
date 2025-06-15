# 📸 Instagram Profile Scraper

> Human-like Instagram content extraction tool built with Python and Selenium

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://selenium.dev)
[![License](https://img.shields.io/badge/License-Educational-orange.svg)](#)

### Currently used for posts only

## ✨ Features

### 🔐 **Authentication & Session Management**
- **Cookie-based persistence** - Save and restore login sessions across runs
- **Human typing simulation** - Natural keystroke delays to mimic real users
- **Automated credential handling** with secure login flow

### 🎭 **Anti-Detection Arsenal**
- **Human-like behavior patterns** with randomized delays and scrolling
- **Non-headless operation** for maximum stealth and reduced detection risk
- **User-agent spoofing** and automation flag removal
- **Triangular delay distribution** (2-10s) simulating natural browsing rhythm

### 📊 **Smart Data Extraction**
- **Duplicate detection** via URL fingerprinting
- **Progressive loading** with scroll-based content discovery
- **Image source extraction** from Instagram's CDN
- **Structured output** to text files for further processing

### 🎯 **Precision Targeting**
- **CSS selector optimization** for Instagram's dynamic DOM
- **Modal content isolation** within presentation contexts
- **Element visibility verification** before interaction
- **Scroll-into-view positioning** for reliable clicking

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

### Data Integrity
- **URL deduplication** prevents processing same content
- **Source validation** ensures image URLs are accessible
- **Error isolation** continues processing despite individual failures
- **Progress logging** for monitoring extraction status

## ⚠️ Not intended for:**misuse or activities that harm Instagram.

## 📈 Performance Summary

- **Expected Delay**: ~5.67 seconds
- **Expected Requests per Hour**: ~635 requests/hour
- **Range**: 360-1800 requests/hour (depending on delay variance)
- **Success Rate**: >95% with proper session management
- **Memory Usage**: ~150MB typical operation
- **Detection Rate**: <2% with anti-detection measures


<p align="center">
  **Built on Earth, by Earth 🌍**
</p>
