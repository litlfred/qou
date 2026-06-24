The recurrence is the matrix identity
$T^{n+1} = T \cdot T^n$, which gives
$(T^{n+1})_{21} = (T)_{11} (T^n)_{21} + (T)_{12} (T^n)_{22}$.
Since $(T)_{11} = q - q^{-1}$ and $(T)_{12} = 1$, and using
$(T^n)_{22} = (T^{n-1})_{21}$ (from $\det T = -1$), this
becomes the Chebyshev recurrence.
$\qquad\blacksquare$
