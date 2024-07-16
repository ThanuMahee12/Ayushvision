import 'package:ayush_plant_idenification_app/view/Screens/OnBoardingScreen.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const AyushApp());
}

class AyushApp extends StatelessWidget {
  const AyushApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'OnBoarding Screen',
      debugShowCheckedModeBanner: false,
      home: OnBoardingScreen(),
    );
  }
}
