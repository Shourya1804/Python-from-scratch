# Python Training Environment

This file explains how to create a Python virtual environment named `python_training` in the workspace.

## Steps to create it

1. Open the terminal in the workspace.
2. Run this command:

```powershell
python -m venv python_training
```

3. Activate the environment:

```powershell
.\python_training\Scripts\activate
```

4. To confirm it is active, you should see `(python_training)` at the start of the terminal prompt.

5. Install packages if needed:

```powershell
pip install -r requirements.txt
```

## To deactivate the environment

```powershell
deactivate
```

## Notes

- Use `python` or `py` depending on your setup.
- If you are on macOS or Linux, use:

```bash
source python_training/bin/activate
```
