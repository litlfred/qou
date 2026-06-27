Let $\mathcal{H}_q^k = \ker\Delta_q \subset \Omega^k(A)$ denote the
space of particles ([$q$-harmonic form](#def:q-harmonic-form)).  The weight
decomposition ([weight decomposition](#def:weight-decomposition)) restricts to
a short exact sequence

```tex
\begin{equation}\label{eq:fermion-boson-ses}
\begin{tikzcd}[column sep=2.5em]
  0 \ar[r]
  & \mathcal{H}_{q,H}^k \ar[r, hook]
  & \mathcal{H}_q^k \ar[r, "\pi_V"]
  & \mathcal{H}_{q,V}^k \ar[r]
  & 0
\end{tikzcd}
\end{equation}
```

where $\mathcal{H}_{q,H}^k = \mathcal{H}_q^k \cap \Omega^k_H(A)$
and $\mathcal{H}_{q,V}^k = \pi_V(\mathcal{H}_q^k)$.  A **boson**
is a particle in the kernel $\mathcal{H}_{q,H}^k$ (purely horizontal:
$\alpha_V = 0$).  A **fermion** is a particle with
$\alpha_V \neq 0$, i.e. one whose image under $\pi_V$ is non-zero.

The sequence splits via $\pi_H$:

```tex
\begin{equation}\label{eq:fermion-boson-split}
\begin{tikzcd}[column sep=2.5em]
  \mathcal{H}_q^k
    \ar[r, "\pi_H \oplus \pi_V", "\sim"']
  & \mathcal{H}_{q,H}^k  \oplus  \mathcal{H}_{q,V}^k
\end{tikzcd}
\qquad
\text{(bosons $\oplus$ fermion vertical parts).}
\end{equation}
```
