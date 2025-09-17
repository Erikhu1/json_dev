
----------------------
Assumptions of use
----------------------

.. aou_req:: AOU-01
  :id: aou_req__docs__01
  :reqtype: Process
  :security: YES
  :safety: ASIL_B
  :status: valid
  :tags: aou

   Problems with nlohmann/json's implementation identified during testing are reported to the upstream nlohmann/json project.


.. aou_req:: AOU-02
  :id: aou_req__docs__02
  :reqtype: Process
  :security: YES
  :safety: ASIL_B
  :status: valid
  :tags: aou

  The build environment used for nlohmann/json in an integrating system is supplied with consistent dependencies.

.. aou_req:: AOU-03
  :id: aou_req__docs__03
  :reqtype: Process
  :security: YES
  :safety: ASIL_B
  :status: valid
  :tags: aou
  
  The integrator has integrator-controlled mirrors of the dependencies.
