# Machine Learning Lösungen im produktiven Einsatz
2 Doppelstunden Vorlesung mit entsprechenden Übungen
 
## Problembeispiel: Vorhersage von Flugverspätungen im US Luftraum
 
An Hand einer Beispielapplikation für die Vorhersage von Flugverspätungen im US Luftraum werden Anforderungen an eine produktionstaugliche Architektur identifiziert und die exemplarische Umsetzung in der Google Cloud beschrieben. Im Vordergrund stehen jeweils Software Engineering und Architekturaspekte und nicht die verwendeten Algorithmen. Mathematische Vorkenntnisse sind nicht erforderlich, Programmierkenntnisse idealerweise in Python von Vorteil.
 
 
## Teil I: Architektur
Vortrag unidirektional. 90 min. (Doppelstunde)

Aufgrund der speziellen Anforderungen, die der Betrieb von Machine Learning Lösungen mit sich bringt, wurden in den vergangenen Jahren neue, potentere Konzepte und Architekturkonzepte entwickelt. Diese Konzepte tragen vor allem dem massiven Einsatz von Daten- und Compute-Kapazitäten Rechnung. Eine produktionstaugliche Gesamtarchitektur muss zudem auch das erhöhte Risiko von Fehlfunktionen konsequent behandeln.
 
### Anforderungen an ML generell
- Performanz
- Resilienz
- Robustheit (gegen Bugs)
- Einfachheit
- Unterstützung f. explorative Entwicklung
- Unterstützung f. statistisches Arbeiten
-                Beobachten mittels TensorBoard.
 
### Anforderungen an den Produktivbetrieb
-                Statistisches Monitoring
-                Value-Monitoring
-                Kontinuierliches Lernen
-                Deployment Modelle – CI/CD
-                A/B Testing
 
### Architekturkomponenten:
-                BigQuery: Petabyte-scale analytical database.
-                DataFlow: Highly parallel data processing pipelines.
-                ML Engine: Machine Learning at scale.
-                Datalab: Exploratives Arbeiten mit Jupyter Notebooks
 
 
## Teil II: Programmiermodell Tensorflow
Vortrag unidirektional. 90 min. (Doppelstunde)

Im zweiten Teil geht es um das Verständnis der Programmierkonzepte und Entwurfsmuster, die zu Erstellung hochperformanter Machine Learning Lösungen eingesetzt werden. Exemplarisch wird Am Beispiel der Tensorflow Python APIs eine komplette ETL und ML Pipeline Implementierung von der Datenbeschaffung bis zum Training eines Modelles besprochen.
 
#### Konzepte und APIs
Gerichtete Graphen: Ein Programmiermodell für High-Performance Computing (GPU/TPU)
Das Kontextproblem: Graph und Session API
tf.data API: Big Data passt nicht in jedes RAM.
-                Tf_transform API: Lösung für das Skew Problem
-                Tf.feature_columns API: Umgang mit sparse input.
Estimator API: Bauanweisungen für gerichtete Graphen.
Lösung für das Resilience Problem: Estimator.train_and_evaluate()
 
 
#### Material:
-                Dokumentierter Source code, Jupyter notebooks on github.
 
Das Lehrkonzept lehnt sich an existierendes Lehrmaterial an, geht aber erheblich intensiver auf die für die Software Entwicklung relevanten Details ein.
 
#### Online Kurse: 
- (https://www.coursera.org/specializations/machine-learning-tensorflow-gcp,
- https://www.coursera.org/specializations/gcp-data-machine-learning )
 
Buch:
V. Lakshmanan, Data Science on the Google Cloud Platform, O'Reilly Media, Inc., 2017. 
ISBN: 9781491974551
 
               
Übungen:
                Noch zu bestimmen.
