The identification of one $q$-bit with one Skein operation unifies several structures in this paper.

### One $q$-bit $=$ one crossing resolution

Each application of the Skein relation

$$
  qL_+ - q^{-1}L_- = (q - q^{-1})L_0
$$

resolves one crossing. The resolution produces exactly one $q$-bit ($= \eta_q$) of information: the choice between the symmetric channel and the antisymmetric channel. The $q$-bit is the information content of this binary choice, weighted by the Hecke eigenvalues.

### Transfer matrix as $q$-bit register

The categorical transfer matrix factorizes the Markov trace over generators:

$$
  \mathrm{tr}_M(\rho(\beta))
  = 
  \prod_{i=0}^{n-2} \hat{V}_i(q).
$$

Each vertex volume $\hat{V}_i$ is a one-point correlation function. The transfer matrix is a register of $q$-bits: each generator $\sigma_i$ stores one $q$-bit, and the Markov trace reads out the entire register. The transfer matrix product is the exact factorization of the $n$-point function into $n-1$ single-$q$-bit evaluations.

### Physical processes as $q$-bit computations

Every physical process in the QOU is a $q$-bit computation:

| Process | $q$-bits consumed | Mechanism |
|---------|-------------------|-----------|
| One Reeb iteration | $1$ $q$-bit | One $f_q$ evaluation on exceptional divisor |
| One Collatz cycle ($v = 2$) | $3$ $q$-bits | $1$ odd step $+ 2$ even steps |
| Beta decay ($T_{3,5}$) | $10$ $q$-bits | $10$-crossing Skein resolution |
| One Planck time | $n_R = q/(q-1)$ $q$-bits | Full Reeb circuit |
| Jones polynomial of $c$-crossing link | $c$ $q$-bits | Full resolution tree |

Beta decay consumes $10$ $q$-bits because the weak boson $T_{3,5} = (\sigma_1 \sigma_2)^5$ has $10$ crossings. Each crossing resolution is one $q$-bit.

### Justification of $Q_{\mathrm{cat}}$

The categorical $Q$-value of a nuclear reaction is the net $q$-bit balance. It is the difference between the $q$-bits stored in the parent braid and the $q$-bits stored in the daughter braids. Because each crossing is one $q$-bit, the $Q$-value is the crossing number difference:

$$
  Q_{\mathrm{cat}}
  = 
  \bigl(c_{\mathrm{parent}} - c_{\mathrm{daughter}}\bigr)
   \cdot  \eta_q
  \quad q\text{-bits}.
$$

The crossing number is the exact $q$-bit content of the braid, and the Skein relation conserves $q$-bits at each resolution step.
