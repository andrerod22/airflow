
 .. Licensed to the Apache Software Foundation (ASF) under one
    or more contributor license agreements.  See the NOTICE file
    distributed with this work for additional information
    regarding copyright ownership.  The ASF licenses this file
    to you under the Apache License, Version 2.0 (the
    "License"); you may not use this file except in compliance
    with the License.  You may obtain a copy of the License at

 ..   http://www.apache.org/licenses/LICENSE-2.0

 .. Unless required by applicable law or agreed to in writing,
    software distributed under the License is distributed on an
    "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    KIND, either express or implied.  See the License for the
    specific language governing permissions and limitations
    under the License.


Package apache-airflow-providers-databricks
------------------------------------------------------

`Databricks <https://databricks.com/>`__


This is detailed commit list of changes for versions provider package: ``databricks``.
For high-level changelog, see :doc:`package information including changelog <index>`.



2.1.0
.....

Latest change: 2021-12-05

=================================================================================================  ===========  =============================================================================
Commit                                                                                             Committed    Subject
=================================================================================================  ===========  =============================================================================
`728e94a47e <https://github.com/apache/airflow/commit/728e94a47e0048829ce67096235d34019be9fac7>`_  2021-12-05   ``Refactor DatabricksHook (#19835)``
`4925b37b66 <https://github.com/apache/airflow/commit/4925b37b661a1117dc9f1a10be11f03e67e1a413>`_  2021-12-04   ``Databricks hook: fix expiration time check (#20036)``
`853576d901 <https://github.com/apache/airflow/commit/853576d9019d2aca8de1d9c587c883dcbe95b46a>`_  2021-11-30   ``Update documentation for November 2021 provider's release (#19882)``
`11998848a4 <https://github.com/apache/airflow/commit/11998848a4b07f255ae8fcd78d6ad549dabea7e6>`_  2021-11-24   ``Databricks: add more methods to represent run state information (#19723)``
`56bdfe7a84 <https://github.com/apache/airflow/commit/56bdfe7a840c25360d596ca94fd11d2ccfadb4ba>`_  2021-11-22   ``Databricks - allow Azure SP authentication on other Azure clouds (#19722)``
`244627e3da <https://github.com/apache/airflow/commit/244627e3daa3e416696e5ddb20a2d4ea5e16b96e>`_  2021-11-14   ``Databricks: allow to specify PAT in Password field (#19585)``
`0a4a8bdb94 <https://github.com/apache/airflow/commit/0a4a8bdb943979820fa7067797764e47f3e0b0c3>`_  2021-11-14   ``Databricks jobs 2.1 (#19544)``
`8ae878953b <https://github.com/apache/airflow/commit/8ae878953b183b2689481f5e5806bc2ccca4c509>`_  2021-11-09   ``Update Databricks API from 2.0 to 2.1 (#19412)``
`28b51fb7bd <https://github.com/apache/airflow/commit/28b51fb7bd886e6a2de216d877cc69147441818e>`_  2021-11-08   ``Authentication with AAD tokens in Databricks provider (#19335)``
`3a0c455855 <https://github.com/apache/airflow/commit/3a0c4558558689d7498fe2fc171ad9a8e132119e>`_  2021-11-07   ``Update Databricks operators to match latest version of API 2.0 (#19443)``
`d9567eb106 <https://github.com/apache/airflow/commit/d9567eb106929b21329c01171fd398fbef2dc6c6>`_  2021-10-29   ``Prepare documentation for October Provider's release (#19321)``
`f5ad26dcdd <https://github.com/apache/airflow/commit/f5ad26dcdd7bcb724992528dce71056965b94d26>`_  2021-10-21   ``Fixup string concatenations (#19099)``
=================================================================================================  ===========  =============================================================================

2.0.2
.....

Latest change: 2021-09-30

=================================================================================================  ===========  ======================================================================================
Commit                                                                                             Committed    Subject
=================================================================================================  ===========  ======================================================================================
`840ea3efb9 <https://github.com/apache/airflow/commit/840ea3efb9533837e9f36b75fa527a0fbafeb23a>`_  2021-09-30   ``Update documentation for September providers release (#18613)``
`ef037e7021 <https://github.com/apache/airflow/commit/ef037e702182e4370cb00c853c4fb0e246a0479c>`_  2021-09-29   ``Static start_date and default arg cleanup for misc. provider example DAGs (#18597)``
`0b7b13372f <https://github.com/apache/airflow/commit/0b7b13372f6dbf18a35d5346d3955f65b31dd00d>`_  2021-09-18   ``Move DB call out of ''DatabricksHook.__init__'' (#18339)``
=================================================================================================  ===========  ======================================================================================

2.0.1
.....

Latest change: 2021-08-30

=================================================================================================  ===========  ============================================================================
Commit                                                                                             Committed    Subject
=================================================================================================  ===========  ============================================================================
`0a68588479 <https://github.com/apache/airflow/commit/0a68588479e34cf175d744ea77b283d9d78ea71a>`_  2021-08-30   ``Add August 2021 Provider's documentation (#17890)``
`be75dcd39c <https://github.com/apache/airflow/commit/be75dcd39cd10264048c86e74110365bd5daf8b7>`_  2021-08-23   ``Update description about the new ''connection-types'' provider meta-data``
`76ed2a49c6 <https://github.com/apache/airflow/commit/76ed2a49c6cd285bf59706cf04f39a7444c382c9>`_  2021-08-19   ``Import Hooks lazily individually in providers manager (#17682)``
`87f408b1e7 <https://github.com/apache/airflow/commit/87f408b1e78968580c760acb275ae5bb042161db>`_  2021-07-26   ``Prepares docs for Rc2 release of July providers (#17116)``
`b916b75079 <https://github.com/apache/airflow/commit/b916b7507921129dc48d6add1bdc4b923b60c9b9>`_  2021-07-15   ``Prepare documentation for July release of providers. (#17015)``
`866a601b76 <https://github.com/apache/airflow/commit/866a601b76e219b3c043e1dbbc8fb22300866351>`_  2021-06-28   ``Removes pylint from our toolchain (#16682)``
=================================================================================================  ===========  ============================================================================

2.0.0
.....

Latest change: 2021-06-18

=================================================================================================  ===========  =================================================================
Commit                                                                                             Committed    Subject
=================================================================================================  ===========  =================================================================
`bbc627a3da <https://github.com/apache/airflow/commit/bbc627a3dab17ba4cf920dd1a26dbed6f5cebfd1>`_  2021-06-18   ``Prepares documentation for rc2 release of Providers (#16501)``
`cbf8001d76 <https://github.com/apache/airflow/commit/cbf8001d7630530773f623a786f9eb319783b33c>`_  2021-06-16   ``Synchronizes updated changelog after buggfix release (#16464)``
`1fba5402bb <https://github.com/apache/airflow/commit/1fba5402bb14b3ffa6429fdc683121935f88472f>`_  2021-06-15   ``More documentation update for June providers release (#16405)``
`9c94b72d44 <https://github.com/apache/airflow/commit/9c94b72d440b18a9e42123d20d48b951712038f9>`_  2021-06-07   ``Updated documentation for June 2021 provider release (#16294)``
`37681bca00 <https://github.com/apache/airflow/commit/37681bca0081dd228ac4047c17631867bba7a66f>`_  2021-05-07   ``Auto-apply apply_default decorator (#15667)``
`807ad32ce5 <https://github.com/apache/airflow/commit/807ad32ce59e001cb3532d98a05fa7d0d7fabb95>`_  2021-05-01   ``Prepares provider release after PIP 21 compatibility (#15576)``
`df143aee8d <https://github.com/apache/airflow/commit/df143aee8d9e7e0089b747bdd27addf63bb4962f>`_  2021-04-29   ``An initial rework of the "Concepts" docs (#15444)``
`49cae1f052 <https://github.com/apache/airflow/commit/49cae1f052ab86369bbc28eb8aba5166b7be7711>`_  2021-04-17   ``Add documentation for Databricks connection (#15410)``
`68e4c4dcb0 <https://github.com/apache/airflow/commit/68e4c4dcb0416eb51a7011a3bb040f1e23d7bba8>`_  2021-03-20   ``Remove Backport Providers (#14886)``
=================================================================================================  ===========  =================================================================

1.0.1
.....

Latest change: 2021-02-04

=================================================================================================  ===========  ========================================================
Commit                                                                                             Committed    Subject
=================================================================================================  ===========  ========================================================
`88bdcfa0df <https://github.com/apache/airflow/commit/88bdcfa0df5bcb4c489486e05826544b428c8f43>`_  2021-02-04   ``Prepare to release a new wave of providers. (#14013)``
`ac2f72c98d <https://github.com/apache/airflow/commit/ac2f72c98dc0821b33721054588adbf2bb53bb0b>`_  2021-02-01   ``Implement provider versioning tools (#13767)``
`a9ac2b040b <https://github.com/apache/airflow/commit/a9ac2b040b64de1aa5d9c2b9def33334e36a8d22>`_  2021-01-23   ``Switch to f-strings using flynt. (#13732)``
`3fd5ef3555 <https://github.com/apache/airflow/commit/3fd5ef355556cf0ad7896bb570bbe4b2eabbf46e>`_  2021-01-21   ``Add missing logos for integrations (#13717)``
`295d66f914 <https://github.com/apache/airflow/commit/295d66f91446a69610576d040ba687b38f1c5d0a>`_  2020-12-30   ``Fix Grammar in PIP warning (#13380)``
`6cf76d7ac0 <https://github.com/apache/airflow/commit/6cf76d7ac01270930de7f105fb26428763ee1d4e>`_  2020-12-18   ``Fix typo in pip upgrade command :( (#13148)``
=================================================================================================  ===========  ========================================================

1.0.0
.....

Latest change: 2020-12-09

=================================================================================================  ===========  ======================================================================================================================================================================
Commit                                                                                             Committed    Subject
=================================================================================================  ===========  ======================================================================================================================================================================
`32971a1a2d <https://github.com/apache/airflow/commit/32971a1a2de1db0b4f7442ed26facdf8d3b7a36f>`_  2020-12-09   ``Updates providers versions to 1.0.0 (#12955)``
`b40dffa085 <https://github.com/apache/airflow/commit/b40dffa08547b610162f8cacfa75847f3c4ca364>`_  2020-12-08   ``Rename remaing modules to match AIP-21 (#12917)``
`9b39f24780 <https://github.com/apache/airflow/commit/9b39f24780e85f859236672e9060b2fbeee81b36>`_  2020-12-08   ``Add support for dynamic connection form fields per provider (#12558)``
`bd90136aaf <https://github.com/apache/airflow/commit/bd90136aaf5035e3234fe545b79a3e4aad21efe2>`_  2020-11-30   ``Move operator guides to provider documentation packages (#12681)``
`c34ef853c8 <https://github.com/apache/airflow/commit/c34ef853c890e08f5468183c03dc8f3f3ce84af2>`_  2020-11-20   ``Separate out documentation building per provider  (#12444)``
`0080354502 <https://github.com/apache/airflow/commit/00803545023b096b8db4fbd6eb473843096d7ce4>`_  2020-11-18   ``Update provider READMEs for 1.0.0b2 batch release (#12449)``
`7ca0b6f121 <https://github.com/apache/airflow/commit/7ca0b6f121c9cec6e25de130f86a56d7c7fbe38c>`_  2020-11-18   ``Enable Markdownlint rule MD003/heading-style/header-style (#12427) (#12438)``
`ae7cb4a1e2 <https://github.com/apache/airflow/commit/ae7cb4a1e2a96351f1976cf5832615e24863e05d>`_  2020-11-17   ``Update wrong commit hash in backport provider changes (#12390)``
`6889a333cf <https://github.com/apache/airflow/commit/6889a333cff001727eb0a66e375544a28c9a5f03>`_  2020-11-15   ``Improvements for operators and hooks ref docs (#12366)``
`7825e8f590 <https://github.com/apache/airflow/commit/7825e8f59034645ab3247229be83a3aa90baece1>`_  2020-11-13   ``Docs installation improvements (#12304)``
`b027223132 <https://github.com/apache/airflow/commit/b0272231320a4975cc39968dec8f0abf7a5cca11>`_  2020-11-13   ``Add install/uninstall api to databricks hook (#12316)``
`85a18e13d9 <https://github.com/apache/airflow/commit/85a18e13d9dec84275283ff69e34704b60d54a75>`_  2020-11-09   ``Point at pypi project pages for cross-dependency of provider packages (#12212)``
`59eb5de78c <https://github.com/apache/airflow/commit/59eb5de78c70ee9c7ae6e4cba5c7a2babb8103ca>`_  2020-11-09   ``Update provider READMEs for up-coming 1.0.0beta1 releases (#12206)``
`b2a28d1590 <https://github.com/apache/airflow/commit/b2a28d1590410630d66966aa1f2b2a049a8c3b32>`_  2020-11-09   ``Moves provider packages scripts to dev (#12082)``
`7e0d08e1f0 <https://github.com/apache/airflow/commit/7e0d08e1f074871307f0eb9e9ae7a66f7ce67626>`_  2020-11-09   ``Add how-to Guide for Databricks operators (#12175)``
`4e8f9cc8d0 <https://github.com/apache/airflow/commit/4e8f9cc8d02b29c325b8a5a76b4837671bdf5f68>`_  2020-11-03   ``Enable Black - Python Auto Formmatter (#9550)``
`8c42cf1b00 <https://github.com/apache/airflow/commit/8c42cf1b00c90f0d7f11b8a3a455381de8e003c5>`_  2020-11-03   ``Use PyUpgrade to use Python 3.6 features (#11447)``
`5a439e84eb <https://github.com/apache/airflow/commit/5a439e84eb6c0544dc6c3d6a9f4ceeb2172cd5d0>`_  2020-10-26   ``Prepare providers release 0.0.2a1 (#11855)``
`872b1566a1 <https://github.com/apache/airflow/commit/872b1566a11cb73297e657ff325161721b296574>`_  2020-10-25   ``Generated backport providers readmes/setup for 2020.10.29 (#11826)``
`349b0811c3 <https://github.com/apache/airflow/commit/349b0811c3022605426ba57d30936240a7c2848a>`_  2020-10-20   ``Add D200 pydocstyle check (#11688)``
`16e7129719 <https://github.com/apache/airflow/commit/16e7129719f1c0940aef2a93bed81368e997a746>`_  2020-10-13   ``Added support for provider packages for Airflow 2.0 (#11487)``
`0a0e1af800 <https://github.com/apache/airflow/commit/0a0e1af80038ef89974c3c8444461fe867945daa>`_  2020-10-03   ``Fix Broken Markdown links in Providers README TOC (#11249)``
`ca4238eb4d <https://github.com/apache/airflow/commit/ca4238eb4d9a2aef70eb641343f59ee706d27d13>`_  2020-10-02   ``Fixed month in backport packages to October (#11242)``
`5220e4c384 <https://github.com/apache/airflow/commit/5220e4c3848a2d2c81c266ef939709df9ce581c5>`_  2020-10-02   ``Prepare Backport release 2020.09.07 (#11238)``
`54353f8745 <https://github.com/apache/airflow/commit/54353f874589f9be236458995147d13e0e763ffc>`_  2020-09-27   ``Increase type coverage for five different providers (#11170)``
`966a06d96b <https://github.com/apache/airflow/commit/966a06d96bbfe330f1d2825f7b7eaa16d43b7a00>`_  2020-09-18   ``Fetching databricks host from connection if not supplied in extras. (#10762)``
`9549274d11 <https://github.com/apache/airflow/commit/9549274d110f689a0bd709db829a4d69e274eed9>`_  2020-09-09   ``Upgrade black to 20.8b1 (#10818)``
`fdd9b6f65b <https://github.com/apache/airflow/commit/fdd9b6f65b608c516b8a062b058972d9a45ec9e3>`_  2020-08-25   ``Enable Black on Providers Packages (#10543)``
`bfefcce0c9 <https://github.com/apache/airflow/commit/bfefcce0c9f273042dd79ff50eb9af032ecacf59>`_  2020-08-25   ``Updated REST API call so GET requests pass payload in query string instead of request body (#10462)``
`3696c34c28 <https://github.com/apache/airflow/commit/3696c34c28c6bc7b442deab999d9ecba24ed0e34>`_  2020-08-24   ``Fix typo in the word "release" (#10528)``
`2f2d8dbfaf <https://github.com/apache/airflow/commit/2f2d8dbfafefb4be3dd80f22f31c649c8498f148>`_  2020-08-25   ``Remove all "noinspection" comments native to IntelliJ (#10525)``
`ee7ca128a1 <https://github.com/apache/airflow/commit/ee7ca128a17937313566f2badb6cc569c614db94>`_  2020-08-22   ``Fix broken Markdown refernces in Providers README (#10483)``
`cdec301254 <https://github.com/apache/airflow/commit/cdec3012542b45d23a05f62d69110944ba542e2a>`_  2020-08-07   ``Add correct signature to all operators and sensors (#10205)``
`7d24b088cd <https://github.com/apache/airflow/commit/7d24b088cd736cfa18f9214e4c9d6ce2d5865f3d>`_  2020-07-25   ``Stop using start_date in default_args in example_dags (2) (#9985)``
`e13a14c873 <https://github.com/apache/airflow/commit/e13a14c8730f4f633d996dd7d3468fe827136a84>`_  2020-06-21   ``Enable & Fix Whitespace related PyDocStyle Checks (#9458)``
`d0e7db4024 <https://github.com/apache/airflow/commit/d0e7db4024806af35e3c9a2cae460fdeedd4d2ec>`_  2020-06-19   ``Fixed release number for fresh release (#9408)``
`12af6a0800 <https://github.com/apache/airflow/commit/12af6a08009b8776e00d8a0aab92363eb8c4e8b1>`_  2020-06-19   ``Final cleanup for 2020.6.23rc1 release preparation (#9404)``
`c7e5bce57f <https://github.com/apache/airflow/commit/c7e5bce57fe7f51cefce4f8a41ce408ac5675d13>`_  2020-06-19   ``Prepare backport release candidate for 2020.6.23rc1 (#9370)``
`f6bd817a3a <https://github.com/apache/airflow/commit/f6bd817a3aac0a16430fc2e3d59c1f17a69a15ac>`_  2020-06-16   ``Introduce 'transfers' packages (#9320)``
`0b0e4f7a4c <https://github.com/apache/airflow/commit/0b0e4f7a4cceff3efe15161fb40b984782760a34>`_  2020-05-26   ``Preparing for RC3 relase of backports (#9026)``
`00642a46d0 <https://github.com/apache/airflow/commit/00642a46d019870c4decb3d0e47c01d6a25cb88c>`_  2020-05-26   ``Fixed name of 20 remaining wrongly named operators. (#8994)``
`f1073381ed <https://github.com/apache/airflow/commit/f1073381ed764a218b2502d15ca28a5b326f9f2d>`_  2020-05-22   ``Add support for spark python and submit tasks in Databricks operator(#8846)``
`375d1ca229 <https://github.com/apache/airflow/commit/375d1ca229464617780623c61c6e8a1bf570c87f>`_  2020-05-19   ``Release candidate 2 for backport packages 2020.05.20 (#8898)``
`12c5e5d8ae <https://github.com/apache/airflow/commit/12c5e5d8ae25fa633efe63ccf4db389e2b796d79>`_  2020-05-17   ``Prepare release candidate for backport packages (#8891)``
`f3521fb0e3 <https://github.com/apache/airflow/commit/f3521fb0e36733d8bd356123e56a453fd37a6dca>`_  2020-05-16   ``Regenerate readme files for backport package release (#8886)``
`92585ca4cb <https://github.com/apache/airflow/commit/92585ca4cb375ac879f4ab331b3a063106eb7b92>`_  2020-05-15   ``Added automated release notes generation for backport operators (#8807)``
`649935e8ce <https://github.com/apache/airflow/commit/649935e8ce906759fdd08884ab1e3db0a03f6953>`_  2020-04-27   ``[AIRFLOW-8472]: 'PATCH' for Databricks hook '_do_api_call' (#8473)``
`16903ba3a6 <https://github.com/apache/airflow/commit/16903ba3a6ee5e61f1c6b5d17a8c6cf3c3a9a7f6>`_  2020-04-24   ``[AIRFLOW-8474]: Adding possibility to get job_id from Databricks run (#8475)``
`5648dfbc30 <https://github.com/apache/airflow/commit/5648dfbc300337b10567ef4e07045ea29d33ec06>`_  2020-03-23   ``Add missing call to Super class in 'amazon', 'cloudant & 'databricks' providers (#7827)``
`3320e432a1 <https://github.com/apache/airflow/commit/3320e432a129476dbc1c55be3b3faa3326a635bc>`_  2020-02-24   ``[AIRFLOW-6817] Lazy-load 'airflow.DAG' to keep user-facing API untouched (#7517)``
`4d03e33c11 <https://github.com/apache/airflow/commit/4d03e33c115018e30fa413c42b16212481ad25cc>`_  2020-02-22   ``[AIRFLOW-6817] remove imports from 'airflow/__init__.py', replaced implicit imports with explicit imports, added entry to 'UPDATING.MD' - squashed/rebased (#7456)``
`97a429f9d0 <https://github.com/apache/airflow/commit/97a429f9d0cf740c5698060ad55f11e93cb57b55>`_  2020-02-02   ``[AIRFLOW-6714] Remove magic comments about UTF-8 (#7338)``
`83c037873f <https://github.com/apache/airflow/commit/83c037873ff694eed67ba8b30f2d9c88b2c7c6f2>`_  2020-01-30   ``[AIRFLOW-6674] Move example_dags in accordance with AIP-21 (#7287)``
`c42a375e79 <https://github.com/apache/airflow/commit/c42a375e799e5adb3f9536616372dc90ff47e6c8>`_  2020-01-27   ``[AIRFLOW-6644][AIP-21] Move service classes to providers package (#7265)``
=================================================================================================  ===========  ======================================================================================================================================================================
