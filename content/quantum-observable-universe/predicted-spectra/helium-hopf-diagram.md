The helium atom $\mathcal{A}(2, 2)$ provides the simplest closed electron shell. Its electron cloud comprises two trefoils $T_{2,3}$ joined by a Hopf link $\mathcal{L}_H$.

```tex
\begin{tikzcd}[row sep=3em, column sep=4em]
  & \boxed{\mathcal{N}(2{,}2)} \ar[dl, "\oplus"', dashed] \ar[dr, "\oplus", dashed] & \\
  T_{2,3} \ar[rr, "\mathcal{L}_H"', "\text{Hopf link}", bend right=15]
  & & T_{2,3} \\
  \underset{e_1}{\text{electron 1}} & \underset{1s^2 \text{ (closed)}}{\text{—————————————}} & \underset{e_2}{\text{electron 2}}
\end{tikzcd}
```

The Hopf link $\mathcal{L}_H$ defines the linking operation between $e_1$ and $e_2$. Each trefoil threads the Seifert surface of the other exactly once ($\mathrm{lk}(e_1, e_2) = 1$).

**Full atom structure.**

$$
  \mathcal{A}(2, 2) = 
  \underbrace{2\mathfrak{p} \oplus 2\mathfrak{n}}_{\alpha\text{-particle}}
   \oplus 
  \underbrace{T_{2,3} \oplus T_{2,3}}_{1s^2\text{ shell (closed)}}
$$

**Closure of the shell.**

The linking matrix of the two-electron Hopf link is:

$$
  L =  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}.
$$

This matrix has rank $1$. Adding a third component $e_3$ requires $\mathrm{lk}(e_3, e_1) \geq 1$ and $\mathrm{lk}(e_3, e_2) \geq 1$. This increases the total linking number from $1$ to at least $3$. The crossing energy cost of these extra links exceeds the binding energy gain. The atom expels the third electron to a higher shell.

**Comparison: lithium ($p = 3$, $n = 4$).**

```tex
\begin{tikzcd}[row sep=2.5em, column sep=3em]
  & \boxed{\mathcal{N}(3{,}4)} \ar[d, "\oplus"', dashed] & \\
  & \underset{1s^2}{\bigl(T_{2,3} \oplus T_{2,3}\bigr)} \ar[d, "\oplus"', dashed, "\text{level 2}"] & \\
  & T_{2,3} & \\
  & \underset{2s^1}{\text{outer electron}} &
\end{tikzcd}
```

$$
  \mathcal{A}(3, 4) = 
  3\mathfrak{p} \oplus 4\mathfrak{n}
   \oplus 
  \underbrace{(T_{2,3} \oplus T_{2,3})}_{1s^2}
   \oplus 
  \underbrace{T_{2,3}}_{2s^1}
$$

The third electron links to the closed $1s^2$ sub-link at a higher linking level. It passes around the entire Hopf pair instead of threading through it. This forms the $2s$ shell. The trefoil links to the $1s^2$ cluster as a single unit.
