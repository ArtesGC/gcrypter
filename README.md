# gcrypter

    Is an encryption algorithm based on bytes and their correspondent numbers to encode strings

- To **Encrypt**:
  - It gets the length of the text given and encode both (text and lenght) into bytes then convert
    the bytes'values into numbers and return a tuple with two tokens (numbers);

- To **Decrypt**:
  - It gets the tuple and retrieve both the values and reconvert them into bytes according to his `bit-length`
  and then decode the byte to the original string (text);
  
## Installation

- Windows:

```sh
pip install gcrypter
```

- Unix/MacOS:

```sh
python3 -m pip install gcrypter
```

or:

```sh
sudo pip3 install gcrypter
```

---

&copy; 2019-2021 [Nurul-GC](https://github.com/Nurul-GC)
&trade; [ArtesGC Inc.](https://artesgc.home.blog)
&trade; [ArtesGC-DevSoft](https://github.com/ArtesGC)
