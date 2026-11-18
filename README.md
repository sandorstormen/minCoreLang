# minCoreLang
minCoreLang is a minimal version of [coreLang](https://github.com/mal-lang/coreLang), a probabilistic modeling and simulation language for the abstract domain of IT. Like coreLang, it is a domain specific language (DSL) created with [MAL (the Meta Attack Language)](https://mal-lang.org/). minCoreLang keeps the core of coreLang and removes a number of assets to give a smaller, more focused language.

## What was removed in minCoreLang

Compared to coreLang, the following assets have been removed, together with their attack steps, defenses and associations:

| Removed asset     | Category          | Also removed                                                                       |
| ----------------- | ----------------- | ---------------------------------------------------------------------------------- |
| `SoftwareProduct` | Compute Resources | Relates to modelling of supply chain attack vectors.                               |
| `IDPS`            | Compute Resources | Relates to modelling attack vectors on the actual defense infrastructure.          |
| `PhysicalZone`    | Compute Resources | Relates to modelling of physical security.                                         |
| `Privileges`      | IAM               | Convenience class that models re-usable sets of permissions.                       |
| `Group`           | IAM               | Convenience class that allows multiple indentities to re-use the same permissions. |
| `RoutingFirewall` | Networking        | Relates to modelling of attack vectors on the actual network firewall.             |

The remaining assets are `Hardware`, `Application`, `Information`, `Data`, `Identity`, `Credentials`, `Network`, `ConnectionRule`, `User`, `SoftwareVulnerability` and `HardwareVulnerability`.

The language ID is `org.mal-lang.minCoreLang` and the entry point is [`minCoreLang.mal`](src/main/mal/minCoreLang.mal), which replaces coreLang's `coreLang.mal`.

## Previous work

| Project                           | Link                                                                |
| --------------------------------- | ------------------------------------------------------------------- |
| coreLang                          | <https://github.com/mal-lang/coreLang>                              |
| Old coreLang                      | <https://github.com/pontusj101/coreLang>                            |
| Core MAL specification of awsLang | <https://gist.github.com/maxwalls/ace99182d064087d2023553337e953c4> |

| Paper                                                                                                                                                                                         | Link                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Katsikeas, S. et al. Development and validation of coreLang: A threat modeling language for the ICT domain, Computers & Security, 2024                                                        | https://doi.org/10.1016/j.cose.2024.104057  |
| Katsikeas, S. et al. Empirical evaluation of a threat modeling language as a cybersecurity assessment tool, Computers & Security, 2024                                                        | https://doi.org/10.1016/j.cose.2024.103743  |
| Katsikeas, S. et al. An Attack Simulation Language for the IT Domain. In: Eades III, H., Gadyatskaya, O. (eds) Graphical Models for Security. GraMSec 2020. Lecture Notes in Computer Science | https://doi.org/10.1007/978-3-030-62230-5_4 |

## License

minCoreLang is derived from coreLang.


Copyright © 2019-2021 [coreLang contributors](https://mal-lang.org/coreLang/contributors.html)

All files distributed in the coreLang project are licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0), except for the following files:

| File                                                                  | License                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`Application.svg`](src/main/resources/icons/Application.svg)         | <img src="src/main/resources/icons/Application.svg" alt="Application.svg" width="32" height="32"/> "[code](https://thenounproject.com/term/code/409495/)" icon by [iconsphere](https://thenounproject.com/iconsphere/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                         |
| [`ConnectionRule.svg`](src/main/resources/icons/ConnectionRule.svg)   | <img src="src/main/resources/icons/ConnectionRule.svg" alt="Connection.svg" width="32" height="32"/> "[connection](https://thenounproject.com/term/connection/2968722/)" icon by [faisalovers](https://thenounproject.com/muhammadfaisal40/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).   |
| [`Credentials.svg`](src/main/resources/icons/Credentials.svg)         | <img src="src/main/resources/icons/Credentials.svg" alt="Credentials.svg" width="32" height="32"/> "[Key](https://thenounproject.com/term/key/2284382/)" icon by [Eagle Eye](https://thenounproject.com/eagleeye/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                             |
| [`Data.svg`](src/main/resources/icons/Data.svg)                       | <img src="src/main/resources/icons/Data.svg" alt="Data.svg" width="32" height="32"/> "[Data](https://thenounproject.com/term/data/1522775/)" icon by [Aybige](https://thenounproject.com/aybigeaya/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                                           |
| [`Exploit.svg`](src/main/resources/icons/Exploit.svg)                 | <img src="src/main/resources/icons/Exploit.svg" alt="Exploit.svg" width="32" height="32"/> "[Biohazard](https://thenounproject.com/term/biohazard/288075/)" icon by [lastspark](https://thenounproject.com/lastspark/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                         |
| [`Identity.svg`](src/main/resources/icons/Identity.svg)               | <img src="src/main/resources/icons/Identity.svg" alt="Identity.svg" width="32" height="32"/> "[identity card](https://thenounproject.com/term/identity-card/2894224/)" icon by [SBTS](https://thenounproject.com/sbts2018/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                    |
| [`Information.svg`](src/main/resources/icons/Information.svg)         | <img src="src/main/resources/icons/Information.svg" alt="Information.svg" width="32" height="32"/> "[Information](https://thenounproject.com/term/information/3267721/)" icon by [Vincencio](https://thenounproject.com/vincenciogilberto/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).    |
| [`Network.svg`](src/main/resources/icons/Network.svg)                 | <img src="src/main/resources/icons/Network.svg" alt="Network.svg" width="32" height="32"/> "[Network](https://thenounproject.com/term/network/2580746/)" icon by [mardjoe](https://thenounproject.com/mereketeheloany/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                        |
| [`PhysicalZone.svg`](src/main/resources/icons/PhysicalZone.svg)       | <img src="src/main/resources/icons/PhysicalZone.svg" alt="PhysicalZone.svg" width="32" height="32"/> "[Location](https://thenounproject.com/term/location/197119/)" icon by [Sergey Novosyolov](https://thenounproject.com/sergey.novosyolov/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/). |
| [`RoutingFirewall.svg`](src/main/resources/icons/RoutingFirewall.svg) | <img src="src/main/resources/icons/RoutingFirewall.svg" alt="RoutingFirewall.svg" width="32" height="32"/> "[Router](https://thenounproject.com/term/router/1602484/)" icon by [SBTS](https://thenounproject.com/sbts2018/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                    |
| [`SoftwareProduct.svg`](src/main/resources/icons/SoftwareProduct.svg) | <img src="src/main/resources/icons/SoftwareProduct.svg" alt="SoftwareProduct.svg" width="32" height="32"/> "[code](https://thenounproject.com/term/code/229789/)" icon by [Cassandra Cappello](https://thenounproject.com/cappellodesigns/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).    |
| [`System.svg`](src/main/resources/icons/System.svg)                   | <img src="src/main/resources/icons/System.svg" alt="System.svg" width="32" height="32"/> "[Server](https://thenounproject.com/term/server/3303099/)" icon by [Icons Field](https://thenounproject.com/iconsdream96/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                           |
| [`User.svg`](src/main/resources/icons/User.svg)                       | <img src="src/main/resources/icons/User.svg" alt="User.svg" width="32" height="32"/> "[profile](https://thenounproject.com/term/profile/2027523/)" icon by [Gagana](https://thenounproject.com/gaganasaki10/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                                  |
| [`Vulnerability.svg`](src/main/resources/icons/Vulnerability.svg)     | <img src="src/main/resources/icons/Vulnerability.svg" alt="Vulnerability.svg" width="32" height="32"/> "[Shield broken](https://thenounproject.com/term/shield-broken/303944/)" icon by [Yuri Mazursky](https://thenounproject.com/colo/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).      |
| [`Group.svg`](src/main/resources/icons/Group.svg)                     | <img src="src/main/resources/icons/Group.svg" alt="Group.svg" width="32" height="32"/> "[group](https://thenounproject.com/term/group/1546821/)" icon by [beth bolton](https://thenounproject.com/bethbolton/) from [the Noun Project](https://thenounproject.com/) is licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).                                 |

See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for details.
