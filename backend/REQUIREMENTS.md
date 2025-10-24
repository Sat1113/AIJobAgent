# Requirements Management

This project uses a two-file approach for Python dependencies:

## 📋 File Explanation

### `requirements.in` - **Main Dependencies** (Hand-curated)
```bash
# Core packages your project directly uses
fastapi==0.119.0
langchain-openai==1.0.0
# ... etc
```

### `requirements.txt` - **Full Dependency Tree** (Generated)
```bash
# All packages including sub-dependencies with exact versions
fastapi==0.119.0
starlette==0.48.0  # sub-dependency of fastapi
pydantic==2.12.3   # sub-dependency of fastapi
# ... 50+ packages total
```

## 🔄 How to Use

### For Development (Recommended)
```bash
# Install all exact versions (reproducible environment)
pip install -r requirements.txt
```

### For Fresh Installs
```bash
# Install main packages (lets pip resolve latest compatible versions)
pip install -r requirements.in
```

### When Adding New Packages
```bash
# 1. Add to requirements.in (manual)
echo "new-package==1.0.0" >> requirements.in

# 2. Install the package
pip install new-package==1.0.0

# 3. Update full requirements (automatic)
pip freeze > requirements.txt
```

## ✅ Benefits of This Approach

- **requirements.in**: Easy to read, shows what YOU actually need
- **requirements.txt**: Exact reproduction, prevents "works on my machine" issues
- **Best of both worlds**: Flexibility + Reproducibility

## 🎯 Which File Should Others Use?

**For production/collaboration**: `requirements.txt` (exact versions)
**For experimentation**: `requirements.in` (flexibility)