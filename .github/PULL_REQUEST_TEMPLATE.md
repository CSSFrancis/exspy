### Requirements
* Read the [contributing guidelines](https://github.com/hyperspy/exspy/blob/main/CONTRIBUTING.rst).
* Fill out the template; it helps the review process and it is useful to summarise the PR.
* This template can be updated during the progression of the PR to summarise its status. 

*You can delete this section after you read it.*

### Description of the change
A few sentences and/or a bulleted list to describe and motivate the change:
- Change A.
- Change B.
- etc.

### Progress of the PR
- [ ] Change implemented (can be split into several points),
- [ ] docstring updated (if appropriate),
- [ ] update user guide (if appropriate),
- [ ] added tests,
- [ ] added line to CHANGES.rst,
- [ ] ready for review.

### Minimal example of the bug fix or the new feature
```python
import exspy
import numpy as np
s = exspy.signals.EELSSpectrum(np.arange(100).reshape(10,10))
# Your new feature...
```


