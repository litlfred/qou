---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-089-262-modular-relations
section_title: "Modular relations"
section_number: 26.2
pages: 134-135
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.895
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
[]{#section:modularity label="section:modularity"}

In order to obtain modular and asymptotic properties for the generating series of theorem [\[theo:Mordell1916\]](#theo:Mordell1916){reference-type="ref" reference="theo:Mordell1916"}, Mordell generalized his results in 1933. We extract the part illustrating our point. Mordell sets: $$f(x) = f(x,\omega) := 
\dfrac{1}{{\text{i}}} \sum_{m~odd} 
\dfrac{(-1)^{(m-1)/2} e^{{\text{i}}\pi (m^{2} \omega/4 + m x)}}{1 + e^{{\text{i}}\pi \omega m}} \cdot$$ This the unique entire function solution of the system: $$\begin{cases}
f(x+1) + f(x) = 0, \\
f(x+\omega) + f(x) = \theta_{1,1}(x).
\end{cases}$$ The interest for Mordell is the (quasi-)modular relation: $$f(x,\omega) - \dfrac{{\text{i}}}{\omega} f(x/\omega,-1/\omega) =
\dfrac{1}{{\text{i}}} \theta_{1,1}(x,\omega) 
\int_{-\infty}^{+\infty} \dfrac{e^{{\text{i}}\pi \omega t^{2} - 2 \pi t x}}
{e^{2 \pi t} - 1} ~ dt.$$ (The path of integration is ${\mathbf R}$ except that one avoids $0$ by below.) The interest for us is that one can put $G(z) := \dfrac{f(x)}{\theta_{1,1}(x)}$ (the right hand side is $1$-periodic), and get the *same* equation as before: $$(\sqrt{q} z \sigma_q- 1) G = \sqrt{q} z.$$ This is used in [@CZMORD] to generalize Mordell results: the fundamental idea is to compare two summations of the solutions, one along the lines of the present paper, the other along different lines previously developped by C. Zhang.
