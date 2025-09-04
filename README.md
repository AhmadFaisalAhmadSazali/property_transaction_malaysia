# Property Transactions in Malaysia – ML Analysis

This project explores property transaction data in Malaysia with a focus on analysis and potential machine learning predictions.  
The dataset is sourced from the **National Property Information Centre (NAPIC)** under JPPH Malaysia.

---

## 📊 Dataset Information

- **Source:** [NAPIC Property Transaction Data](https://napic2.jpph.gov.my/ms/data-transaksi?category=36&id=241)  
- **Date Extracted:** 1st September 2025 
- **Preprocessing:** After downloading the csv file it normally fails `pandas.read_csv`, open it and resave it as csv utf-8 format.
- **Coverage:** Property transactions across Malaysia  

### Columns
- `Property Type` – Type of property (e.g., 1–1½ Storey Semi-Detached, Terrace, Condominium, etc.)  
- `District` – District where the transaction occurred  
- `Mukim` – Sub-district administrative area  
- `Scheme Name/Area` – Name of the housing scheme, township, or development area  
- `Road Name` – Street name or road location of the property  
- `Transaction Date` – Full date of the transaction in `DD/MM/YYYY` format  
- `Tenure` – Tenure of the property (e.g., Freehold, Leasehold)  
- `Land/Parcel Area` – Size of land parcel, typically in square meters (`sq.m`)  
- `Unit` – Unit number of the property (if applicable)  
- `Main Floor Area` – Built-up area of the property in square meters (`sq.m`)  
- `Unit Level` – Floor level of the property (for high-rise units)  
- `Transaction Price` – Price of the transaction in Malaysian Ringgit (RM)  

---

## ⚙️ Project Goals
1. Clean and preprocess the raw transaction dataset.  
2. Perform exploratory data analysis (EDA).  
3. Identify key trends in property transactions across districts and property types.  
4. Develop machine learning models to predict property transaction prices.  

---

## 📂 Project Structure
