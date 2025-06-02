# Coding Guidelines for lmnp-tax-engine Agents

1. **Dependencies**  
   * PyYAML and Pydantic are available.  
   * Do **NOT** replace them with custom parsers or data classes.

2. **Patch scope**  
   * Touch only the file(s) mentioned in the task description.  
   * One issue = one failing test = one fix.

3. **Workflow**  
   * Always begin by adding a failing pytest.  
   * Run `poetry run pytest -q`; iterate until green.  
   * Do not commit formatting-only changes.

4. **Decimal accuracy**  
   * Use `Decimal` for all monetary values.  
   * Never mix `float` with `Decimal`.
