---
doc_id: arxiv-1301.6953v1
doc_title: "Chiral Perturbation Theory and Mesons"
section_id: sec-005-6-leading-logarithms
section_title: "Leading logarithms"
section_number: 6
pages: 10-13
source_pdf: 1301.6953v1.pdf
source_sha256: 8c9231d0832df3b6
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.995
latex_coverage_ratio: 0.585
doc_brief: "Chiral Perturbation Theory and Mesons — 7 sections: Front matter; Chiral Perturbation Theory; Introduction"
---
The last part on which I want to report is some recent progress
in calculating leading logarithms in effective field theories.
Some of this is also mentioned in the talk by Kampf \cite{Kampf}.
The underlying argument goes something like:
Take a quantity with a single scale: $F(M)$.
The dependence on the scale in field theory is typically
logarithmic, so with $L=\log\left(\mu/M\right)$we get
\begin{equation}
F= F_0 + F_1^1 {L} + F^1_0 + F_2^2{ L^2} + F^2_1 L + F^2_0 
+ F_3^3{ L^3}
 +\cdots
\end{equation}
The leading logarithms are the terms with $F_m^m{ L^m}$.
The $F_m^m$ can be more easily calculated than the
 full result. This follows from the fact that for any physical quantity
$\mu\left( dF/d\mu\right)\equiv 0$ and 
ultraviolet divergences in Quantum Field Theory are always local.
In renormalizable theories this is embedded in the renormalization group but for
effective field theories such as QCD there is no simple recursive argument.
Weinberg already argued that one can get away with only one-loop calculations
to obtain the leading logarithms \cite{Weinberg0}. This was proven in \cite{BC0} and in a somewhat simpler way in \cite{BC1}. The underlying reason is that the cancellation of nonlocal divergences gives a set of consistency relations
between contributions of different loop order as explained in \cite{BCEGS}.
In the massless case \cite{Polyakov1,Polyakov2,Polyakov3} this leads to
an almost analytic expression to very high orders since the diagrams remain
fairly simple to all orders. In the massive case diagrams with any number of
external legs show up but the whole process can be automatized since
in \cite{BC1} it was realized that the Lagrangians at higher order do not need
to be minimal. Obtaining the minimal Lagrangian at each order would have been
essentially impossible. In the massive case all published results relate to
the $O(N)$ model, masses in \cite{BC1}, decay constants and vacuum expectation
values as well as form-factors and meson-meson scattering in \cite{BC2} and
the anomalous sector \cite{BKL}. Extension to $SU(N)\times SU(N)$ has been
done in the massless case \cite{Polyakov3} and is in progress for the massive
case.
I refer to the original papers for more results but a few highlights are
that the large $N$ (number of flavours) limit is not a good approximation
for any of the quantities calculated. The series seem to converge
in the expected regions. None of the leading logarithms calculated seems
to be unusually large. Unfortunately the hope that we might recognize
the general result for arbitrary $N$ proved in vain.

\acknowledgments
I thank the organizers for a very pleasant meeting and my collaborators in the
various parts reported here.
This work is supported in part by the European Community-Research
Integrating Activity ``Study of Strongly Interacting Matter''
(HadronPhysics3, Grant Agreement No. 283286)
and the Swedish Research Council grants 621-2011-5080 and 621-2010-3326.
