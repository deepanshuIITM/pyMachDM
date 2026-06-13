# **pyMachDM: Machine Learning-Based Decision-Makers in Python**

<div class="sidebar-badges">
  <a href="https://github.com/deepanshuIITM/pyMachDM"><img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="Version"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</div>

**pyMachDM** is an open-source Python package that benchmarks interactive multi-criteria decision-making (iMCDM) methods by simulating human preferences using machine learning-based decision makers (Machine-DM).


**`pip install pyMachDM`**


## **Features**

Furthermore, our framework offers a variety of different features which cover various facets of benchmarking iMCDM methods:

<div class="grid cards" markdown>


-   📢 **Announcement** 

    ---

    Release of **pyMachDM** 



-   [💻 <span style="color: inherit !important;">**Interface**</span>](home/quickstart.md)

    ---

    Main entry point function to run your Machine-DM:
    
    * **`machine_dm`**

-   [:test_tube: <span style="color: inherit !important;">**Benchmark Problems**</span>](bench-imcdm/problems/bench_probs.md)

    ---

    Built-in benchmark test suits:

    * **Single-objective:** Ackley, Griewank, Rastrigin
    * **Multi-objective:** ZDT1, DTLZ2


-   [:balance_scale: <span style="color: inherit !important;"> **Interactive MCDMs**</span>](imcdm/overview.md)

    ---

    List of interactive MCDM Methods:

    * [NIMBUS](imcdm/methods/nimbus.md)
    * [STEM](imcdm/methods/stem.md)
    * [GUESS](imcdm/methods/guess.md), etc.

-   [:robot: <span style="color: inherit !important;"> **Machine-DM**</span>](mach-dm/machdm.md)

    ---

    Components of Machine-DM:

    * [Class Predictor ML](mach-dm/class_predictor.md)
    * [Parameter Predictor ML](mach-dm/parameter_predictor.md)
    * [Preference Evaluator Metric](mach-dm/preference_evaluator.md)

-   [🎯 <span style="color: inherit !important;"> **Bench-iMCDM**</span>](bench-imcdm/overview.md)

    ---

    Benchmarking iMCDM Methods:

    * [Bench-iMCDM framework](bench-imcdm/overview.md)
    * [Pre-trained ANNs](bench-imcdm/pretrained.md)
    * [Performance Metrics](bench-imcdm/metrics.md)

-   [📊 <span style="color: inherit !important;">  **Visualization**</span>](visualization.md)

    ---

    Visualization methods:

    * [Two-dimensional](visualization.md/#bi-objective-problems)
    * [Three-dimensional](visualization.md/#three-objective-problems)
    * [More than three-dimensional](visualization.md/#many-objective-problems)

-   [🎓 <span style="color: inherit !important;"> **Tutorial**</span>](tutorials/tutorials.md)

    ---

    Tutorial on Basics:

    * [Core Idea](tutorials/core_idea.md)
    * [Demo](tutorials/demo.md)
    * [Live Script](tutorials/live_script.md)

</div>


