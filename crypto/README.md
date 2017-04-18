# Crypto Homework 1:

## Lecture slides at:
https://docs.google.com/presentation/d/1Z1ZjkiCngGUtwXEHsrk2C87fEdK2mYkkxzaPIa9dkXs/edit?usp=sharing

### Question 1: 

Decrypt vcipher.txt and find the flag - (Note: non-alpha characters should be unaltered, but do consume a part of the cycle - i.e. the 3rd character uses the 3rd character of the key). Don't use automated tools and show your work.

### Question 2:

Decrypt feistel.bin - this file has been encrypted with:
8 round feistel structure
key == str2num("thisisakey")

with F box:

```python
def F(block, key):
    s = num2str(str2num(block) ^ key)
    return s[1:] + s[0]
```
    
    
### Question 3:

Decrypt otpcipher.bin - remember that all of these flags start with 'flag{'


