import 'package:flutter/material.dart';
import 'package:my_app/pages/home_page.dart';
import 'package:my_app/pages/login_page.dart';
import 'package:my_app/utils/Constants.dart';

Future main() async {
  WidgetsFlutterBinding.ensureInitialized();

  Constants c = new Constants();
  bool loggedInStatus = await c.getLoggedInStatus();

  runApp(MaterialApp(
    title: "Awesome App",
    home: loggedInStatus ? HomePage() : LoginPage(),
    theme: ThemeData(primarySwatch: Colors.purple),
    routes: {
      "/login": (context) => LoginPage(),
      "/home": (context) => HomePage()
    },
  ));
}
