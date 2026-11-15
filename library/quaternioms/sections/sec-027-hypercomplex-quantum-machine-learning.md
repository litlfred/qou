---
doc_id: quaternioms
doc_title: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations"
section_id: sec-027-hypercomplex-quantum-machine-learning
section_title: "Hypercomplex Quantum Machine Learning"
section_number: null
pages: 25-25
source_pdf: quaternioms.pdf
source_sha256: becedcbc858611dd
toc_source: outline
doc_brief: "Quaternionic and Octonionic Frameworks for Quantum Computation: Mathematical Structures, Models, and Fundamental Limitations — 45 sections: Front matter; Introduction; Extended Related Work"
---
Quantum Machine Learning (QML) is a rapidly developing ﬁeld that seeks to leverage
quantum principles and hardware to enhance machine learning algorithms. The introduc-
tion of hypercomplex numbers offers a new avenue for QML, potentially leading to more
expressive models, more compact data representations, and improved performance for
certain types of data or tasks.
Quaternionic Quantum Neural Networks (QNNs)
The natural ability of quaternions to represent rotations in 3D space makes them partic-
ularly well-suited for machine learning tasks that involve spatial data, orientations, or color
images (which have three color channels) [21]. In classical machine learning, quaternionic
neural networks (QNNs) have already demonstrated advantages in terms of reduced pa-
rameter counts, faster convergence, and enhanced generalization capabilities compared to
their real- or complex-valued counterparts, especially for data where underlying rotational
symmetries are important [21].
Extending this to the quantum domain, a quaternionic quantum neural network
(QQNN) could utilize quaternionic qubits as its fundamental processing units or incor-
porate quaternionic gate operations within a variational quantum circuit. In a QQNN
layer, the weights, biases, and activations could be quaternionic, leading to a more compact
representation of the network’s parameters [21]. This could be particularly advantageous in
variational quantum algorithms (VQAs) used for QML, where the optimization landscape
might be smoother or more easily navigable when parameterized by quaternions. The key
beneﬁts of QQNNs in QML would include the following:
•
Compact Data Encoding: Quaternions can encode more information per parameter
compared to real or complex numbers. For example, a single quaternion can naturally
represent a 3D vector and an orientation, potentially reducing the number of logical
qubits or qudits required to encode certain features.
•
Exploiting Rotational Symmetries: For datasets with inherent rotational symmetries
(e.g., medical images, robotics data, physical simulations), QQNNs could natively
incorporate these symmetries, leading to more efﬁcient learning and better generaliza-
tion, similar to how convolutional neural networks exploit translational symmetries.
•
Reduced Parameter Space: By using quaternionic weights and biases, the total number
of trainable parameters in a quantum neural network could be signiﬁcantly reduced,
potentially alleviating issues like barren plateaus in VQAs.
