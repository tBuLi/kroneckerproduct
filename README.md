(this is a work in progress, nothing works yet)

Kronecker Product
=================

This plugin is made to make working with direct products very easy and efficient.

```python
>>> unit, x, y, z = pauli_matrices()
>>> x << unit
sigma_{x} ⊗ 1
```

Direct product are done using the bitshift operator <<, since we are essentially 
pushing the matrix on the right hand side of the operator into whats on the left 
hand side.

The normal multiplication operator still does matrix multiplication:

```python
>>> unit, x, y, z = pauli_matrices()
>>> x * y
i sigma_{z}
```

The usecase I'm developing this for is doing matrix multiplication with block matrices build up by taking the Kronecker product of many 2 x 2 matrices. If we take the Kronecker product of k such matrices, the dimension of the final matrix will therefore be 2^k x 2^k. For large k this will become impossible very quickly. However, by our knowledge that the final matrix is in fact a kronecker product, we only have to multiply the k 2 x 2 matrices to arrive at the result.

So roughly speaking,
(2^k * 2^k) * (2^k * 2^k) -> k * (2 * 2) * (2 * 2)

This is a huge decrease in computational complexity!

Obviously, because of the OOP implementation the overhead will be far greater but I expect that for large k this will start to pay of. Furthermore, the k multiplications of 2 * 2 matrices could even be done in parallel.

Lazy Evaluation FTW
===================

No matrix multiplication is performed when calculating kronecker products. 
In fact, the objects do not have to be matrices at all. This package only cares whether the 
object have multiplication defined.

Matrix multiplication of the irreducable blocks is performed when you actually perform a matrix multiplication using * since

![Matrix Product](https://upload.wikimedia.org/math/2/e/0/2e0c63f797f7adfe945e59b2b8d751d9.png)

Properties
==========
Bilinearity and Associativity
-----------------------------
```python
A << (B + C) == (A << B) + (A << C)
(A + B) << C == (A << C) + (B << C)
(k*A) << B == k(A << B)
(A << B) << C == A << (B << C)
```
Matrix Product
--------------
```python
(A << B) * (C << D) == (A * C) << (B * D)
```
Inverse
-------
```python
1/(A << B) == 1/A << 1/B
```
This might be a slight abuse of notation, but I think it is a good one in the context of coding with matrices. The division operator is out of a job anyway.

Transpose and Conjugation
-------------------------
```python
(A << B).T == A.T << B.T
~(A << B) == ~A << ~B
```
Conjugation uses the binary ``not`` operator, since we flip the imaginary 'bit'.

Determinant
-----------
```python
det(A << B) == det(A)**len(B) * det(B)**len(A)
```
Exponentiation
--------------
Not defined yet.

More Examples
=============
```python
>>> unit, x, y, z = pauli_matrices()
>>> (x + y) << unit
sigma_{x} + sigma{y}
```

```python
>>> a = x << x
>>> b = y << y
>>> a * b
(i sigma_z) ⊗ (i sigma_z)
```

```python
>>> a = x << x
>>> 1/a
(sigma_x)^{-1} ⊗ (sigma_x)^{-1}
```

