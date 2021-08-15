import 'package:flutter/material.dart';

class BgImage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Image.asset(
      "assets/images/bg.webp",
      fit: BoxFit.cover,
    );
  }
}
