---
doc_id: arxiv-hep-th-0006156v1
doc_title: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality"
section_id: sec-027-62-analytic-properties
section_title: "Analytic properties"
section_number: 6.2
pages: 15-16
source_pdf: 0006156v1.pdf
source_sha256: b799d4ef150291cf
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.891
latex_coverage_ratio: 0.897
doc_brief: "Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality — The quantum discrete Liouville model in the strongly cou- pled regime, 1 < c < 25, is formulated as a well"
---
We can perform the integration in ([\[ncqdl\]](#ncqdl){reference-type="ref" reference="ncqdl"}) by the residue method. The result can be written as ratio of two q-exponentials $$\label{ratio}
e_b(z)=
(e^{2\pi (z+c_b)b};q^2)_\infty/
(e^{2\pi (z-c_b)b^{-1}};\bar q^2)_\infty,$$ where $$q=e^{i\pi b^2},\quad \bar q=e^{-i\pi b^{-2}},$$ thus reprpoducing definition ([\[eq:fofz\]](#eq:fofz){reference-type="ref" reference="eq:fofz"}) in the text. Formula ([\[ratio\]](#ratio){reference-type="ref" reference="ratio"}) defines a meromorphic function on the entire complex plane, satisfying functional equations ([\[inversion\]](#inversion){reference-type="ref" reference="inversion"}) and ([\[shift\]](#shift){reference-type="ref" reference="shift"}), with essential singularity at infinity. So, it is the analytical continuation of definition ([\[ncqdl\]](#ncqdl){reference-type="ref" reference="ncqdl"}) to the entire complex plane. It is easy to read off location of its poles and zeroes: $$\mathrm{zeroes\ of\ }(e_b(z))^{\pm1}=
\{\mp(c_b+mib+nib^{-1}):\ m,n\in\mathbb Z_{\ge0}\}.$$ The behavior at infinity depends on the direction along which the limit is taken: $$\label{asymp}
e_b(z)\bigg\vert_{|z|\to\infty} \approx\left\{
\begin{array}{ll}
1&|\arg(z)|>\frac{\pi}{2}+\arg(b);\\
e^{i\pi z^2-i\pi (1+2c_b^2)/6}&|\arg(z)|<\frac{\pi}{2}-\arg(b);\\
(\bar q^2;\bar q^2)_\infty/\Theta(ib^{-1}z;-b^{-2})&
|\arg z-\pi/2|<\arg b;\\
\Theta(ibz;b^{2})/(q^2; q^2)_\infty&
|\arg z+\pi/2|<\arg b,
\end{array}\right.$$ where $$\Theta(z;\tau)\equiv\sum_{n\in\mathbb Z}e^{i\pi\tau n^2+2\pi i
  nz}, \quad\Im\tau>0.$$ Thus, for complex $b$, double quasi-periodic $\theta$-functions, generators of the field of meromorphic functions on complex tori, describe the asymptotic behavior of the non-compact QDL.
