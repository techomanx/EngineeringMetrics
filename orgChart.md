:::mermaid
flowchart TD
    DirectPlatforms["Direct Platforms, Channel Mainframes, PWC, IBM, DP, Autopay, ISO Arch"]
    DirectPlatforms --> ManishTiwari["Manish Tiwari"]

    %% Engineering
    subgraph Engineering
        LitheshAnargha["Lithesh Anargha"]
        ShaunMort["Shaun Mort"]
        TBC1["TBC1"]
        TBC2["TBC2"]
    end
    ManishTiwari --> LitheshAnargha
    ManishTiwari --> ShaunMort
    ShaunMort --> TBC1
    ShaunMort --> TBC2

    %% Architecture
    subgraph Architecture
        Virendra
        SoniaJain["Sonia Jain"]
    end
    ManishTiwari --> Virendra
    ManishTiwari --> SoniaJain

    %% Delivery
    subgraph Delivery
        NathanSvatosky["Nathan Svatosky"]
        AmitGoswami["Amit Goswami (India Rep)"]
    end
    ManishTiwari --> NathanSvatosky
    NathanSvatosky --> AmitGoswami

    %% Analysis
    subgraph Analysis
        KarunaGupta["Karuna Gupta"]
        C11QE["C11 - Hands on QE"]
    end
    ManishTiwari --> KarunaGupta
    KarunaGupta --> C11QE

    %% Quality Assurance
    subgraph QualityAssurance
        ShilpiKhandelwal["Shilpi Khandelwal"]
        ArnabKundu["Arnab Kundu"]
        Sudhakar["Sudhakar 50%"]
        TBC
        Hussain
        RichardB["Richard B"]
    end
    ManishTiwari --> ShilpiKhandelwal
    ShilpiKhandelwal --> ArnabKundu
    ArnabKundu --> Sudhakar
    ArnabKundu --> TBC
    ArnabKundu --> Hussain
    ArnabKundu --> RichardB

    %% Release Operation
    subgraph ReleaseOperation
        Ramki
        OpeISO["Ope (ISO)"]
        AshMalik["Ash Malik"]
        ShipraGoyalISO["Shipra Goyal (ISO)"]
    end
    ManishTiwari --> Ramki
    Ramki --> OpeISO
    OpeISO --> AshMalik
    AshMalik --> ShipraGoyalISO

    %% Infra Support
    subgraph InfraSupport
        AccoliteTeam["Accolite Team"]
        NidhiArora["Nidhi Arora"]
        GauravKumara["Gaurav Kumara"]
        PawanGupta["Pawan Gupta"]
        ShairKhan["Shair Khan"]
        IndiaLEs["India LEs"]
    end
    ManishTiwari --> AccoliteTeam
    AccoliteTeam --> NidhiArora
    AccoliteTeam --> GauravKumara
    AccoliteTeam --> PawanGupta
    AccoliteTeam --> ShairKhan
    AccoliteTeam --> IndiaLEs

    %% Programme Support
    subgraph ProgrammeSupport
        PeteTBC["Pete/TBC (BLT,Reg,Disc)"]
    end
    ManishTiwari --> PeteTBC

    %% Others directly under Manish
    ManishTiwari --> Thanos
    ManishTiwari --> AndrewK
    ManishTiwari --> VinayP
    ManishTiwari --> GarethHaigh
:::

---
```plantuml
@startyaml
organization:
  - id: DirectPlatforms
    name: "Direct Platforms, Channel Mainframes, PWC, IBM, DP, Autopay, ISO Arch"
    children:
      - id: ManishTiwari
        name: "Manish Tiwari"
        children:
          - id: LitheshAnargha
            name: "Lithesh Anargha"
          - id: ShaunMort
            name: "Shaun Mort"
            children:
              - id: TBC1
                name: "TBC1"
              - id: TBC2
                name: "TBC2"
          - id: Virendra
            name: "Virendra"
          - id: SoniaJain
            name: "Sonia Jain"
          - id: KarunaGupta
            name: "Karuna Gupta"
            children:
              - id: C11QE
                name: "C11 - Hands on QE"
          - id: NathanSvatosky
            name: "Nathan Svatosky"
            children:
              - id: AmitGoswami
                name: "Amit Goswami (India Rep)"
          - id: ShilpiKhandelwal
            name: "Shilpi Khandelwal"
            children:
              - id: ArnabKundu
                name: "Arnab Kundu"
                children:
                  - id: Sudhakar
                    name: "Sudhakar (50%)"
                  - id: TBC
                    name: "TBC"
                  - id: Hussain
                    name: "Hussain"
                  - id: RichardB
                    name: "Richard B"
          - id: Thanos
            name: "Thanos"
          - id: AndrewK
            name: "Andrew K"
          - id: VinayP
            name: "Vinay P"
          - id: GarethHaigh
            name: "Gareth Haigh"
          - id: Ramki
            name: "Ramki"
            children:
              - id: OpeISO
                name: "Ope (ISO)"
                children:
                  - id: AshMalik
                    name: "Ash Malik"
                    children:
                      - id: ShipraGoyalISO
                        name: "Shipra Goyal (ISO)"
                        children:
                          - id: Aparna
                            name: "Aparna"
                          - id: Arthi
                            name: "Arthi"
                          - id: Sravanthi
                            name: "Sravanthi"
          - id: PeteTBC
            name: "Pete/TBC (BLT, Reg, Disc)"
          - id: AccoliteTeam
            name: "Accolite Team"
            children:
              - id: NidhiArora
                name: "Nidhi Arora"
              - id: GauravKumara
                name: "Gaurav Kumara"
              - id: PawanGupta
                name: "Pawan Gupta"
              - id: ShairKhan
                name: "Shair Khan"
              - id
@endyaml

----
```plantuml
@startuml
!define RECTANGLE class

package "Engineering" {
    RECTANGLE LitheshAnargha
    RECTANGLE ShaunMort
    RECTANGLE TBC1
    RECTANGLE TBC2
}

package "Architecture" {
    RECTANGLE Virendra
    RECTANGLE SoniaJain
}

package "Delivery" {
    RECTANGLE NathanSvatosky
    RECTANGLE AmitGoswami
}

package "Analysis" {
    RECTANGLE KarunaGupta
    RECTANGLE C11QE
}

package "Quality Assurance" {
    RECTANGLE ShilpiKhandelwal
}

package "Release Operation" {
    RECTANGLE Ramki
    RECTANGLE OpeISO
    RECTANGLE AshMalik
    RECTANGLE ShipraGoyalISO
}

package "Infra Support" {
    RECTANGLE AccoliteTeam
    RECTANGLE NidhiArora
    RECTANGLE GauravKumara
    RECTANGLE PawanGupta
    RECTANGLE ShairKhan
    RECTANGLE IndiaLEs
}

package "Programme Support" {
    RECTANGLE PeteTBC
}

' Now define links
LitheshAnargha --> ManishTiwari
ShaunMort --> ManishTiwari
TBC1 --> ShaunMort
TBC2 --> ShaunMort
Virendra --> ManishTiwari
SoniaJain --> ManishTiwari
NathanSvatosky --> ManishTiwari
AmitGoswami --> NathanSvatosky
KarunaGupta --> ManishTiwari
C11QE --> KarunaGupta
ShilpiKhandelwal --> ManishTiwari
Ramki --> ManishTiwari
OpeISO --> Ramki
AshMalik --> OpeISO
ShipraGoyalISO --> AshMalik


@enduml