import pandas as pd

# خواندن فایل CSV
df = pd.read_csv('Snappfood - Sentiment Analysis.csv')

# لیست‌های خالی برای ذخیره داده‌ها
comments = []
labels = []
label_ids = []

# پردازش هر سطر
for row in df['commentlabellabel_id']:
    if 'HAPPY0' in str(row):
        # جدا کردن با split
        parts = str(row).split('HAPPY0')
        comment = parts[0].strip()
        label = 'HAPPY'
        label_id = 0
    elif 'SAD1' in str(row):
        # جدا کردن با split
        parts = str(row).split('SAD1')
        comment = parts[0].strip()
        label = 'SAD'
        label_id = 1
    else:
        # اگه پترن پیدا نشد
        comment = str(row)
        label = 'UNKNOWN'
        label_id = -1

    # اضافه کردن به لیست‌ها
    comments.append(comment)
    labels.append(label)
    label_ids.append(label_id)

# ساخت دیتافریم جدید
clean_df = pd.DataFrame({
    'comment': comments,
    'label': labels,
    'label_id': label_ids
})

# ذخیره فایل جدید
clean_df.to_csv('clean_data.csv', index=False)

# نمایش نتیجه
print(f"تعداد کل: {len(clean_df)}")
print(f"HAPPY: {len(clean_df[clean_df['label'] == 'HAPPY'])}")
print(f"SAD: {len(clean_df[clean_df['label'] == 'SAD'])}")
print("\nنمونه داده‌ها:")
print(clean_df.head())