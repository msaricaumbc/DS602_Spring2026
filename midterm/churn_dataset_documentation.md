# Streaming Service Customer Churn Prediction

## Business Context

**StreamFlix** is a popular streaming service that wants to identify customers who are likely to cancel their subscription within the next 30 days. Early identification allows the company to implement targeted retention strategies (personalized recommendations, offers, support outreach) to reduce churn and maintain revenue.

This is a **binary classification** task: you have labeled data and must build a model to predict `will_churn` (0 = will not churn, 1 = will churn).

## Dataset Overview

- **Total Records**: 10,000
- **Features**: 37
- **Target Variable**: `will_churn` (0 or 1)
- **Missing Values**: 2,500
- **Churn Rate**: 18.89%
- **Class Distribution**: {0: 8111, 1: 1889}

## Feature Categories

### 1. Subscription Features
- `subscription_start_date`: Date when customer first subscribed
- `subscription_length_days`, `subscription_length_months`: Tenure
- `subscription_plan`: basic, standard, premium, family, student
- `monthly_price`: Monthly subscription price ($)
- `billing_cycle`: monthly, annual
- `payment_method`: credit_card, debit_card, paypal, apple_pay, google_pay, bank_transfer

### 2. Usage Behavioral Features (Last 30 Days)
- `total_watch_time_hours`, `sessions_count`, `avg_session_duration_minutes`
- `days_since_last_watch`, `unique_titles_watched`, `content_completion_rate`
- `abandoned_series_count`, `binge_sessions_count`

### 3. Content Preference Features
- `primary_genre`, `genres_watched_count`, `genres_watched` (text)
- `content_type_preference`: movies, tv_shows, both
- `new_content_ratio`

### 4. Device and Platform Features
- `primary_device`, `devices_used_count`, `devices_used` (text), `primary_os`

### 5. Engagement and Interaction Features
- `has_profile`, `number_of_profiles`, `watchlist_size`
- `ratings_given_count`, `reviews_written_count`, `downloads_count`

### 6. Support and Service Features
- `support_tickets_count`, `support_ticket_reasons` (text)
- `payment_failures_count`, `account_on_hold`, `used_free_trial`

### 7. Temporal Features
- `current_month`, `days_until_next_billing`

### 8. Target
- `will_churn`: 1 if customer will churn in the next 30 days, 0 otherwise

