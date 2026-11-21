---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-008-32-quantization
section_title: "Quantization"
section_number: 3.2
pages: 17-18
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
toc_source: outline
text_source: latex
latex_prose_ratio: 0.923
latex_coverage_ratio: 1.0
doc_brief: "Quantum Field Theory and the Volume Conjecture — 15 sections: Front matter; Preliminaries; The many dimensions of the volume"
---
[]{#sec:quant label="sec:quant"}

The basic problem of quantization begins with a pair $({\cal M},\omega)$, where ${\cal M}$ is a manifold with symplectic structure $\omega$, called a classical "phase space." Quantization takes this pair and constructs a quantum Hilbert space ${\cal H}$. Moreover, quantization should map the algebra of functions on ${\cal M}$ to an algebra ${\cal A}_{\hbar}$ of operators on ${\cal H}$:

$$\begin{array}{ccc}
 (M,\omega) & \leadsto & {\cal H}~(=\text{Hilbert space}) \\
  && \raisebox{-.1cm}{\includegraphics[width=.5cm]{actsbelow}} \\
 \text{alg. of functions on ${\cal M}$} & \leadsto & \text{alg. of operators on ${\cal H}$} \\
 f & \mapsto & {\cal O}_f :{\cal H}\to{\cal H}\,.
\end{array}$$

The functions on ${\cal M}$ form a Poisson algebra with respect to the usual pointwise multiplication of functions and a Lie algebra structure $\{\bullet,\bullet\}$ induced by the symplectic structure. Quantization must map this algebra to an associative but noncommutative algebra ${\cal A}_{\hbar}$, such that

$$= -i\hbar\, {\cal O}_{\{f,g\}} + \ldots \,,$$

where $[\bullet,\bullet]$ is the commutator of operators. Here $\hbar$ is a parameter that is involved in the determination of ${\cal H}$ itself as well as the algebra of operators.

Very roughly, the Hilbert space ${\cal H}$ consists of $L^2$ sections of a complex line bundle over ${\cal M}$ with curvature $\frac{1}{\hbar}\omega$. Locally, these sections are only allowed to depend on *half* of the coordinates of ${\cal M}$. In a standard physical setup, ${\cal M}$ can be thought of as the space of all possible positions $x_i$ and momenta $p_i$ of particles; thus the elements of ${\cal H}$ are functions ("wavefunctions") that depend on either positions or moments, but not both.

In addition to the construction of ${\cal H}$, the process of quantization must also explain how classical motions or trajectories of a physical system are associated to quantum states in ${\cal H}$. A classical trajectory (or "semiclassical state") is described by a Lagrangian submanifold ${\cal L}\subset{\cal M}$. Being Lagrangian means that ${\cal L}$ is middle-dimensional and $\omega|_{\cal L}=0$. Let $\theta$ be 1-form (called a Liouville 1-form

[^1])

that satisfies $\omega = d\theta$. Notice that $\theta|_{\cal L}$ is closed. Then the Lagrangian ${\cal L}$ is called quantizable if

$$\oint_\gamma \theta \in 2\pi \hbar\, {\mathbb{Z}}\label{thetaq}$$

for any closed cycle $\gamma\subset{\cal L}$. The vector (or wavefunction) $Z\in{\cal H}$ corresponding to ${\cal L}$ can be written as

$$Z = Z(x) = \exp\left( \frac{i}{\hbar}S_0(x) + \ldots\right)\,, \label{v}$$

with

$$S_0(x) = \int_{x_0}^x \theta$$

for some fixed $x_0$ and varying $x\in{\cal L}$. Due to the quantization [\[thetaq\]](#thetaq){reference-type="eqref" reference="thetaq"}, the expression [\[v\]](#v){reference-type="eqref" reference="v"} is completely well-defined.

Expression [\[v\]](#v){reference-type="eqref" reference="v"} only defines $Z$ to leading order in $\hbar$. To find subleading corrections, it is useful to employ a complementary approach. Suppose that the Lagrangian submanifold ${\cal L}$ is cut out by certain equations $f_i=0$ on ${\cal M}$. Quantization promotes these functions to operators ${\cal O}_{f_i}$ acting on ${\cal H}$, and the vector $Z$ can also be defined as a solution to the equations

$${\cal O}_{f_i}\cdot Z = 0  \qquad\forall\; i\,.$$

If the ${\cal O}_{f_i}$ are properly quantized, then the solution to these equations will be the exact wavefunction.

[^1]: There is an ambiguity in choosing $\theta$, directly related to the choice of coordinates of ${\cal M}$ (positions versus momenta) that elements of ${\cal H}$ are to depend on.
