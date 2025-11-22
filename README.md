<div align="center">
  <h1>Korcen</h1>
</div>

<div align="center">
  
  [![PyPI version](https://img.shields.io/pypi/v/korcen.svg?style=flat-square)](https://pypi.org/project/korcen)
  [![downloads](https://img.shields.io/pepy/dt/korcen.svg?style=flat-square)](https://pypi.org/project/korcen/)
</div>

"Easy and Powerful Korean Profanity Filtering, Now Accessible to Everyone!"

Korcen is a Python library for keyword-based profanity filtering, specifically optimized for the Korean language. It provides a straightforward way to integrate profanity detection into various applications, helping to maintain a cleaner and safer communication environment.

Other versions of Korcen include:
*   [Korcen.ts](https://github.com/KR-korcen/korcen.ts): A TypeScript version of Korcen.
*   [Korcen-go](https://github.com/fluffy-melli/korcen-go): A Go version of Korcen, developed by fluffy-melli.
*   [Korcen-kogpt2](https://github.com/Tanat05/korcen-kogpt2): An experimental version of Korcen exploring KoGPT2 integration.

## Features
- Optimized for Korean profanity detection.
- Simple integration and usage.
- Keyword-based filtering.
- Customizable include/exclude lists for profanity terms.
- Ability to highlight and mask profane words.
- Supports categorization of profanity (e.g., general, sexual, belittling, etc.).
- Provides boolean checks for profanity presence.

## Installation
To install Korcen, run the following command:
```sh
pip install korcen
```

## Usage
Here's a basic example of how to use Korcen:

```python
from korcen import korcen

text_with_profanity = "이런 ㅈ같은 경우를 봤나."
text_without_profanity = "정말 좋은 날씨입니다."

# Check for profanity (returns True if profanity is found)
print(f"'{text_with_profanity}': {korcen.check(text_with_profanity)}")
print(f"'{text_without_profanity}': {korcen.check(text_without_profanity)}")

# Highlight profanity (replaces profanity with asterisks)
highlighted_text = korcen.highlight_profanity(text_with_profanity)
print(f"Highlighted: {highlighted_text}")

# Example with a placeholder for a stronger profanity
text_with_strong_profanity = "이런 씨X, 정말 최악이야."
print(f"'{text_with_strong_profanity}': {korcen.check(text_with_strong_profanity)}")
highlighted_strong_text = korcen.highlight_profanity(text_with_strong_profanity)
print(f"Highlighted (strong): {highlighted_strong_text}")

```

For more detailed examples, including custom filter configurations and checks for various profanity types, please see `EXAMPLES.md` (Note: This file will need to be created in a subsequent step).

## Contributing
Contributions are welcome! If you'd like to help improve Korcen, please feel free to fork the repository, make your changes, and submit a pull request.

If you plan to add new features or make significant changes, please open an issue first to discuss your ideas.

## License
Distributed under the MIT License. See `LICENSE` for more information.
