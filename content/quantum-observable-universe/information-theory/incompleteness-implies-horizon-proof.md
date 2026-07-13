*Proof.*
Define the **diagonal function**:

$$
  d(n) = \mathrm{eval}(e(n))(n) + 1.
$$

For any program $p \in P$, surjectivity provides an index $n$ such that $e(n) = p$. Then:

$$
  d(n) = \mathrm{eval}(p)(n) + 1 \neq \mathrm{eval}(p)(n).
$$

Consequently, $d \neq \mathrm{eval}(p)$. Because $p$ was arbitrary, $d \notin \mathrm{im}(\mathrm{eval})$. $\square$

**Necessity of $\mathbb{N}$-embedding.**

The diagonal argument builds $d$ by evaluating program $e(n)$ on input $n$. This self-application imposes two requirements:

1. **Countability of programs**: The map $e$ must surject from $\mathbb{N}$ onto $P$, indexing programs by natural numbers. In the QOU, the braid group $B_n$ on $n$ strands is finitely generated and thus countable. The set of all finite braids $\bigsqcup_n B_n$ forms a countable union of countable sets, satisfying the requirement.

2. **$\mathbb{N}$ as input domain**: Programs must compute functions $\mathbb{N} \to \mathbb{N}$, requiring the system to represent and manipulate natural numbers. The QOU satisfies this via Turing completeness ([Skein Turing machine](#rem:skein-turing-machine)). Each Toffoli gate acts on bit strings ($\{0,1\}^n \hookrightarrow \mathbb{N}$), and the Skein polynomial evaluates to values that distinguish inputs.

If programs are uncountable, or if the system cannot represent $\mathbb{N}$, the diagonal construction fails. The computable fragment might then span the entire function space. A trivial category (one object, one morphism) remains vacuously "Turing-complete," but it hosts no non-computable sections because it lacks arithmetic encoding.

**Connection to the computational horizon.**

Each non-computable function $d$ corresponds to a section $E_d \in \Gamma(\mathcal{S}, A_0)$ that evades factorization through any finite braid ([non-computable bundles](#rem:skein-turing-machine)). These sections populate the computational horizon $\mathcal{H}_c = V(\mathfrak{h}_c)$ ([computational horizon](#def:computational-horizon)):

$$
  E_d \in \Gamma(\mathcal{S}, A_0) \setminus \Gamma_{\mathrm{fin}}(\mathcal{S}, A_0)
  \quad\Longrightarrow\quad
  \mathcal{H}_c \neq \varnothing.
$$

The proposition ensures that such $E_d$ exist whenever the system meets arithmetic non-triviality. The computational horizon represents a necessary feature of any Turing-complete resolution system equipped with $\mathbb{N}$-embedding. It is a direct consequence of the system's expressive power, not a contingent property of specific NP-complete links.
