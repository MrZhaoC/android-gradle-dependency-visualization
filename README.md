# android-gradle-dependency-visualization
## Android gradle dependency tree print
```
  .\gradlew :app:dependencies --configuration releaseRuntimeClasspath
```
```
+--- androidx.navigation:navigation-fragment:2.5.1
|    +--- androidx.fragment:fragment-ktx:1.5.1
|    |    +--- androidx.activity:activity-ktx:1.5.1 (*)
|    |    +--- androidx.collection:collection-ktx:1.1.0 (*)
|    |    +--- androidx.core:core-ktx:1.2.0 (*)
|    |    +--- androidx.fragment:fragment:1.5.1 (*)
|    |    +--- androidx.lifecycle:lifecycle-livedata-core-ktx:2.5.1
|    |    |    +--- androidx.lifecycle:lifecycle-livedata-core:2.5.1 (*)
|    |    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.6.21 (*)
|    |    +--- androidx.lifecycle:lifecycle-viewmodel-ktx:2.5.1 (*)
|    |    +--- androidx.savedstate:savedstate-ktx:1.2.0 (*)
|    |    \--- org.jetbrains.kotlin:kotlin-stdlib:1.6.21 (*)
|    +--- androidx.navigation:navigation-runtime:2.5.1 (*)
     \--- androidx.collection:collection:1.0.0 -> 1.1.0 (*)

```

## save dependency tree to file
  save dependecy tree to dependencies.txt.
## run py file to get result
example：androidx.savedstate:savedstate:1.2.0
### project dependency chain
```
androidx.lifecycle:lifecycle-viewmodel-savedstate:2.5.1-->androidx.savedstate:savedstate:1.2.0
androidx.activity:activity:1.2.4 -> 1.5.1-->androidx.savedstate:savedstate:1.2.0
androidx.fragment:fragment:1.3.6 -> 1.5.1-->androidx.savedstate:savedstate:1.2.0
com.android.support:appcompat-v7:24.2.1 -> androidx.appcompat:appcompat:1.4.2-->androidx.savedstate:savedstate:1.1.0 -> 1.2.0
androidx.savedstate:savedstate-ktx:1.2.0-->androidx.savedstate:savedstate:1.2.0
```
### real dependency in project
```
androidx.appcompat:appcompat:1.4.2
androidx.activity:activity:1.5.1
androidx.lifecycle:lifecycle-viewmodel-savedstate:2.5.1
androidx.fragment:fragment:1.5.1
androidx.savedstate:savedstate-ktx:1.2.0
```
  
  
