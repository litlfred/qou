Direct multiplication of the $2\times 2$ generating matrices over $\mathbb{Z}[t^{\pm 1}]$ (with $q = t^2$ and $q^{-1} = t^{-2}$) gives

$$
  L_+
  = \rho(\sigma_0)\rho(\sigma_1)
  = \begin{pmatrix} q & 1 \\ 0 & -q^{-1} \end{pmatrix}
    \begin{pmatrix} -q^{-1} & 0 \\ 1 & q \end{pmatrix}
  = \begin{pmatrix} 0 & q \\ -q^{-1} & -1 \end{pmatrix}
$$

and

$$
  L_-
  = \rho(\sigma_1)\rho(\sigma_0)
  = \begin{pmatrix} -q^{-1} & 0 \\ 1 & q \end{pmatrix}
    \begin{pmatrix} q & 1 \\ 0 & -q^{-1} \end{pmatrix}
  = \begin{pmatrix} -1 & -q^{-1} \\ q & 0 \end{pmatrix}.
$$

Squaring $L_+$ and $L_-$ and forming the mixed product $L_+ L_-$ yields

$$
  L_+^2 = \begin{pmatrix} -1 & -q \\ q^{-1} & 0 \end{pmatrix},
  \qquad
  L_-^2 = \begin{pmatrix} 0 & q^{-1} \\ -q & -1 \end{pmatrix},
  \qquad
  L_+ L_- = \begin{pmatrix} q^2 & 0 \\ q^{-1} - q & q^{-2} \end{pmatrix}.
$$

Adding the squares and scaling the mixed product by $2$,

$$
  L_+^2 + L_-^2
  = \begin{pmatrix} -1 & q^{-1} - q \\ q^{-1} - q & -1 \end{pmatrix},
  \qquad
  2\,L_+ L_-
  = \begin{pmatrix} 2q^2 & 0 \\ 2(q^{-1} - q) & 2q^{-2} \end{pmatrix}.
$$

At entry $(0,0)$, the left-hand matrix has Laurent polynomial $-1 = -t^0 \in \mathbb{Z}[t^{\pm 1}]$, whose degree-$4$ coefficient is $0$, whereas the right-hand matrix has $2q^2 = 2t^4 \in \mathbb{Z}[t^{\pm 1}]$, whose degree-$4$ coefficient is $2 \neq 0$. Hence $-1 \neq 2q^2$ in $\mathbb{Z}[t^{\pm 1}]$, and therefore $L_+^2 + L_-^2 \neq 2\,L_+ L_-$.
