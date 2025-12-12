
### RSA Secure Messaging System

This project implements a complete RSA-based secure messaging system, including user authentication, key generation, encryption, decryption, and an interactive messaging interface. The system provides a full end-to-end demonstration of public-key cryptography, modular arithmetic, and secure communication principles without relying on external cryptographic libraries.

The project includes an implementation of fundamental number-theoretic algorithms used in cryptography. These include fast modular exponentiation for efficient computation of a^n mod b, the Euclidean Algorithm for computing greatest common divisors, and the Extended Euclidean Algorithm for producing modular inverses. Together, these are used to construct RSA key pairs by generating public keys, private keys, and the modulus n from two prime inputs.

Users can either supply their own prime numbers or allow the system to generate random primes based on a configurable bit length. Once primes are processed, the application computes Euler’s totient, finds a valid public exponent e, and calculates the private exponent d through modular inversion. The system then uses these values to encode plaintext messages character by character and decode ciphertext back to readable text.

A credential-based login system provides controlled access. Users can sign in with existing accounts, create new accounts, or exit. Passwords and usernames are stored in a dictionary structure, and the system enforces a limited number of login attempts. After authentication, users access a menu that allows them to send messages, receive encrypted messages, or automatically decode their previously sent ciphertext.

Message encoding converts characters to ASCII integers before encrypting them using RSA. Decoding performs the reverse, decrypting numerical blocks and translating them back into human-readable characters. The interface includes error handling for invalid primes, malformed encrypted inputs, and attempts to decode without possessing correct keys.

This project demonstrates secure communication concepts, manual construction of RSA encryption primitives, defensive programming, and user-oriented system design. It functions both as a practical encryption tool and an educational implementation of classical public-key cryptography.
