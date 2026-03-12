# E-commerce Customer Purchase Prediction

## Business Context

**Company A Solutions** is an e-commerce analytics company hired by online retailers to predict which customers are likely to make a purchase during their browsing session. This helps optimize marketing spend, personalize user experience in real-time, and improve conversion rates.

This is a **binary classification** task: you have labeled data and must build a model to predict `will_purchase` (0 = will not purchase, 1 = will purchase).

## Dataset Overview

- **Total Records**: 10,000
- **Features**: 26
- **Target Variable**: `will_purchase` (0 or 1)
- **Missing Values**: 2,000
- **Purchase Rate**: 51.41%
- **Class Distribution**: {1: 5141, 0: 4859}

## Feature Categories

### 1. Temporal Features
- `session_start_time`: Timestamp when session began
- `hour`: Hour of day (0-23)
- `day_of_week`: Day of week (0=Monday, 6=Sunday)
- `month`: Month (1-12)
- `is_weekend`: Binary flag for weekend (1) vs weekday (0)
- `session_duration_minutes`: Length of session in minutes
- `days_since_last_visit`: Days since customer's last visit

### 2. Behavioral Numerical Features
- `page_views`: Number of pages viewed during session
- `clicks`: Number of clicks made during session
- `avg_scroll_depth`: Average scroll depth (0-1)
- `items_added_to_cart`: Number of items added to cart
- `items_removed_from_cart`: Number of items removed from cart
- `search_queries_count`: Number of search queries made
- `product_page_time_minutes`: Time spent on product pages
- `categories_viewed_count`: Number of different categories viewed
- `avg_price_viewed`: Average price of products viewed ($)

### 3. Categorical Features
- `device_type`: mobile, desktop, tablet
- `traffic_source`: organic_search, paid_search, social_media, email, direct, referral
- `customer_segment`: new_customer, returning_customer, vip_customer, at_risk_customer
- `region`: North_America, Europe, Asia_Pacific, Latin_America, Middle_East_Africa
- `browser`: Chrome, Safari, Firefox, Edge, Other
- `operating_system`: Windows, macOS, iOS, Android, Linux
- `user_type`: new_user, returning_user

### 4. Text Features
- `search_queries`: Comma-separated search terms used
- `categories_viewed`: Comma-separated product categories viewed
- `user_agent`: Browser user agent string

### 5. Target
- `will_purchase`: 1 if customer made (or will make) a purchase in the session, 0 otherwise

