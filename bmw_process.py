import pandas as pd
import sqlite3

# 1. ዳታ ምንባብ (እቲ ስም ፋይል ልክዕ ከምቲ ዝመጸልካ ጽሓፎ)
try:
    df = pd.read_excel('bmw_global_sales_dataset.xlsx')
    print("✅ ፋይል ብዓወት ተነቢቡ ኣሎ!")
except Exception as e:
    print(f"❌ ጌጋ፦ {e}")

# 2. ትንተና (Analysis) - እንታይ ዓይነት ዓውድታት (Columns) ኣለዉዎ?
print("\n📊 እዞም ዓውድታት (Columns) ተረኺቦም፦")
print(df.columns.tolist())

# 3. ምስ SQL Database ምርካብ (እንተዘየለ ባዕሉ ይፈጥሮ)
conn = sqlite3.connect('bmw_sales.db')

# 4. ምስጋግር (Table ስሙ 'sales' ይበሃል)
df.to_sql('sales', conn, if_exists='replace', index=False)

print("\n🚀 ዳታ ናብ SQL ተሰጋጊሩ ኣሎ! ሕጂ 'bmw_sales.db' ተፈጢሩ ኣሎ።")
conn.close()
