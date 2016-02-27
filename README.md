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

Lazy Evaluation FTW
===================

No matrix multiplication is performed if you don't want it too. In fact, the 
objects do not have to be matrices at all. This package only cares whether the 
object have multiplication defined.

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
(sigma_x)^{-1} ⊗ (sigma_x{-1}
```

