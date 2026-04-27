# Fake Profile Detection

## Business Context

**SocialTrust Analytics** is a social media trust and safety analytics company hired by online platforms to identify accounts that may be fake, spam-oriented, or suspicious. The goal is to help moderation teams prioritize accounts for review while still giving analysts enough information to explain why an account looks risky.

This dataset does NOT include the target variable in the main student file. The data scientist must analyze the unlabeled profile data, engineer useful features, discover natural account groups, and assign likely fake-profile labels before checking the separate evaluation labels.

## Dataset Overview

- **Total Records**: 5,000
- **Features**: 19 
- **Target Variable**: NOT INCLUDED 
- **Missing Values**: 0
- **Class Distribution in Labels File**: 3,198 normal profiles and 1,802 fake profiles
- **Fake Profile Rate**: 36.04%

## Feature Categories

### 1. Account Profile Features
- `profile_id`: Unique profile identifier
- `account_age_days`: Age of the account in days
- `bio_length`: Number of characters in the profile bio
- `profile_picture_quality`: Profile image quality score from 0 to 1
- `external_link_count`: Number of external links in the profile
- `username_digit_count`: Number of digits in the username
- `username_length`: Username length

### 2. Audience and Network Features
- `followers_count`: Number of followers
- `following_count`: Number of accounts followed

### 3. Posting Activity Features
- `posts_count`: Lifetime number of posts
- `posts_last_30_days`: Number of posts made in the last 30 days
- `recent_posts_sampled`: Number of recent posts reviewed for behavior signals
- `avg_caption_length`: Average caption length for sampled recent posts
- `repeated_captions`: Number of repeated captions in sampled recent posts
- `night_posts`: Number of sampled posts made during nighttime hours

### 4. Engagement Features
- `likes_last_20_posts`: Total likes across the most recent 20 posts
- `comments_last_20_posts`: Total comments across the most recent 20 posts

### 5. Direct Message Features
- `dm_sent_last_7_days`: Number of direct messages sent in the last 7 days
- `dm_replies_last_7_days`: Number of direct message replies received in the last 7 days

### 6. Evaluation Target
- `fake_profile`: Hidden binary target where 1 means the account behaves like a fake or suspicious profile and 0 means the account behaves like a normal profile

## Important Feature Engineering Ideas

The raw columns are intentionally incomplete on their own. Students should create ratios, rates, and interaction features before clustering or modeling.

## Expected Profile Patterns

### 1. Normal Established Profiles
Older accounts with better profile picture quality, longer bios, healthier follower/following ratios, lower duplicate caption rates, and stronger comment quality. These profiles are usually `fake_profile = 0`.

### 2. Suspicious Growth or Spam Profiles
Newer accounts with high following counts, weak follower/following ratios, more digits in usernames, repeated captions, high night posting, and high direct message pressure. These profiles are usually `fake_profile = 1`.

### 3. Ambiguous Creator or Brand-Like Profiles
Some real profiles may post often, include external links, or follow many accounts. These cases make the clusters overlap and require students to justify labeling decisions instead of relying on a single feature.

## Using the Subject Matter Expert (SME)

The SME class allows you to query label for a specific `profile_id`. It should be treated like a limited expert resource rather than as a dataset to inspect directly.

### Example Usage:

```python
from fake_profile_sme import SME

# Initialize SME
sme = SME()

fake_profile = sme.ask("P00001")

print(f"Fake profile: {fake_profile}")
```

### Important Notes:
- You can ask up to 500 times
- Pass one `profile_id` string to `sme.ask()`
- `sme.ask(profile_id)` returns `0` for a likely normal profile and `1` for a fake or suspicious profile
- Do not use `fake_profiles_labels.csv` during the initial clustering and label creation process
- Scale numeric features before using distance-based clustering methods
- Inspect cluster centers and summary statistics before assigning labels
- Ambiguous clusters are expected and should be discussed in the analysis
- Compare student-created labels against `fake_profile` only at the end, after the semi-supervised workflow is complete
