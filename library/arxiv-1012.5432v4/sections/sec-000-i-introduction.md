---
doc_id: arxiv-1012.5432v4
doc_title: "Towards topological quantum computation? Knotting and fusing flux tubes"
section_id: sec-000-i-introduction
section_title: "I Introduction"
section_number: null
pages: 3-4
source_pdf: 1012.5432v4.pdf
source_sha256: ec5f6da1f813649e
toc_source: outline
text_source: latex
latex_prose_ratio: 0.994
latex_coverage_ratio: 1.0
doc_brief: "Towards topological quantum computation? Knotting and fusing flux tubes — 56 sections: Front matter; I Introduction; II (2+1)-dimensional Topological G"
---
Richard Feynman in 1982 was the first to conceive of the idea of a computer based on quantum mechanics as potentially offering more computational power than computers based on just classical physics. [@Feynman] As computer components are beginning to attain distances on which quantum mechanical effects can no longer be ignored, continued size reduction would necessitate the design of a system that thrives on quantum mechanical distance scales.

In addition, subsequent developments in algorithms have shown that certain problems believed to be classically computationally intractable would be efficiently solvable on a quantum computer. (Notably, quantum algorithms for factoring large numbers and finding discrete logs efficiently [@shor] would be able to decipher RSA and Diffie-Hellman, a fact which would have radical implications for the security of data ranging from credit cards to electronic communication). These algorithms would suggest even the asymptotic computational power of a device is inextricably linked to the underlying physical mechanisms governing its operation in this more general framework. (The Church-Turing thesis asserts that all classical devices lead to the same asymptotic complexity.)

The main idea of topological quantum computation is to exploit in an automatically scalable way the physics of the underlying system to obtain computations that are inherently protected from errors. Thus the issue of quantum error correction on the software level is sidestepped to a certain extent as error-prevention is a physical property of the system (effectively hardwired). From the computational perspective, the Threshold Theorem (as discovered by A. Steane in [@steane] and D. Aharonov and M. Ben-Or in [@Or]) guarantees that errorless quantum computation can be achieved using quantum error correction as long as the original error rate is below a fixed threshold. However, even if the current threshold estimate (1 part in $10^{-4}$) is attainable, the overhead required to accomplish the error correction procedure is impractical - in general, thousands of qubits are required in order to obtain the desired control over one. As it stands, topological accuracy may even be necessary to achieve the threshold.

Information is stored in the global topology of the system and processed via fusion and braiding. Since the environment interacts locally and the global topology of the system is not effected by local perturbations, the system is inherently protected against decoherence.
