// swift-tools-version: 6.1
import PackageDescription

let package = Package(
    name: "NeonVibe",
    platforms: [
        .macOS(.v14),
    ],
    targets: [
        .executableTarget(
            name: "NeonVibe",
            path: "Sources/NeonVibe",
            resources: [
                .process("Resources"),
            ])
    ]
)
