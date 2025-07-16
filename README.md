# 🧠 Concur Account String Generator

The **Concur Account String Generator** is a lightweight desktop application built to streamline the generation of department-level account strings for import into SAP Concur's custom fields based on employee inputs. Designed with data quality, validation, and transformation principles in mind, it simplifies a tedious manual process into a fast, repeatable, and structured output pipeline.

---

## 📊 Why This Project Matters

Manual entry of structured cost and Accounting data is prone to errors, inconsistencies, and delays. This tool leverages Python’s data handling strengths and robust GUI design to:

- Ensure **input consistency**
- Speed up data entry
- **Validate critical data constraints**
- Apply **standardized transformations**
- Export structured output ready for integration

It serves as a practical example of data engineering principles applied in an operational context.

---

## 🧱 Key Features

- 🧩 **GUI interface** for data entry (Tkinter)
- ⚙️ **Modular architecture** separating logic, UI, and error handling
- ✅ **Robust validation**: missing fields, mismatched lengths, invalid values
- 📁 **Excel output** in a clean, analysis-ready format
- 🧪 Designed with data pipelines and batch processing in mind
- 🧠 Easy for non-technical users to understand and run

---

## 🧑‍💻 Tech Stack

| Area                | Tools / Libraries        |
|---------------------|--------------------------|
| GUI                 | Tkinter                  |
| Data Transformation | Pandas                   |
| Error Handling      | Custom Python exceptions |
| Packaging           | PyInstaller              |

---

## 📂 Folder Structure

```
ConcurAcctStringGenerator/
├── app/
│   ├── main.py           # GUI and entry point
│   ├── logic.py          # Input processing and file generation
│   ├── utils.py          # Helper and UI functions
│   ├── errors.py         # Custom error classes
│   ├── README.txt        # In-app help file
```

---

## 🧠 Engineering Highlights

- **Validation Pipeline**  
  Structured error classes handle conditions like:
  - Empty or missing values
  - Inconsistent list lengths
  - Invalid department or delete flag codes

- **Modular Design**  
  Codebase is broken into single-responsibility modules, making it extensible for future:
  - Input file uploads
  - Database connectivity
  - API-based validation

- **Reproducibility**  
  Outputs are consistent and formatted for ingestion into enterprise systems or further analysis.

---

## 📈 Output Example

Each run exports an `output.xlsx` file with schema:

| DELETE | NAME        | LEVEL_01_CODE | LEVEL_02_CODE | LEVEL_03_CODE | LEVEL_04_CODE |
|--------|-------------|---------------|----------------|----------------|----------------|
| N      | Jane A Doe  | Moonbase Ops  | 123            | 82011          | CATEGORY_X     |
| N      | Jane A Doe  | Moonbase Ops  | 123            | 82013          | CATEGORY_X     |
| N      | Jane A Doe  | Moonbase Ops  | 123            | 82021          | CATEGORY_X     |
| N      | Jane A Doe  | Moonbase Ops  | 123            | 82101          | CATEGORY_X     |
| N      | Jane A Doe  | Moonbase Ops  | 123            | 82888          | CATEGORY_X     |
| N      | Jane A Doe  | Moonbase Ops  | 123            | 82014          | CATEGORY_X     |
---

## 🚀 Getting Started

### 1. Run the App (source)
```bash
python -m app.main
```

### 2. Build Executable (optional)
```bash
pyinstaller ConcurAcctStringGenerator.spec
```

### 3. Distribute the `.exe` in `/dist` – no Python install required

---

## 🛠 Future Ideas

- Load input from CSV
- Department code editor
- Direct integration with ERP or SAP systems
- Audit trail or logging

---

## 📬 Feedback & Contributions

This project was designed for internal automation, but if you find it useful or want to extend it for your own analytics needs, feel free to open an issue or fork the repo.

---

## 📄 License

MIT License
