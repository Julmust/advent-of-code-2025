Before running any command, make sure you know what directory you're in by using the `pwd` bash command.

Use all best practises for Python including, but not limited to:
* Comments
* Docstrings
* Type hints
* Code structure

Use uv as a virtual environment manager

Any resources spun up for testing must be torn down.

All code should be using python 3.12 and package management should be done using uv. Both of these are already installed on the system.

If you start a resource for testing, it should always be torn down afterwards

Package Management
- ONLY use uv, NEVER pip
- Installation: uv add package
- Running tools: uv run tool
- Upgrading: uv add --dev package --upgrade-package package
- FORBIDDEN: uv pip install, @latest syntax 

Code Quality
- Type hints and docstrings required for all code
- Functions must be focused and small
- Follow existing patterns exactly
- Line length: 100 chars maximum
- Add logging
- Add comment where it makes sense

Code Style
- PEP 8 naming (snake_case for functions/variables)
- Class names in PascalCase
- Constants in UPPER_SNAKE_CASE
- Document with docstrings
- Use f-strings for formatting, the exception to this is logging which should use lazy syntax

Development Philosophy
- Simplicity: Write simple, straightforward code
- Readability: Make code easy to understand
- Performance: Consider performance without sacrificing readability
- Maintainability: Write code that's easy to update
- Testability: Ensure code is testable
- Reusability: Create reusable components and functions
- Less Code = Less Debt: Minimize code footprint

Coding Best Practices
– Early Returns: Use to avoid nested conditions
– Descriptive Names: Use clear variable/function names (prefix handlers with "handle")
– Constants Over Functions: Use constants where possible
– DRY Code: Don't repeat yourself
– Functional Style: Prefer functional, immutable approaches when not verbose
– Minimal Changes: Only modify code related to the task at hand
– Function Ordering: Define composing functions before their components
– TODO Comments: Mark issues in existing code with "TODO:" prefix
– Simplicity: Prioritize simplicity and readability over clever solutions
– Build Iteratively Start with minimal functionality and verify it works before adding complexity
– Run Tests: Test your code frequently with realistic inputs and validate outputs
– Build Test Environments: Create testing environments for components that are difficult to validate directly
– Functional Code: Use functional and stateless approaches where they improve clarity
– Clean logic: Keep core logic clean and push implementation details to the edges
– File Organsiation: Balance file organization with simplicity - use an appropriate number of files for the project scale