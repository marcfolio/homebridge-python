var Service;
var Characteristic;
var exec = require('child_process').exec;
var light;

module.exports = function(homebridge) {
  Service = homebridge.hap.Service;
  Characteristic = homebridge.hap.Characteristic;
  homebridge.registerAccessory('homebridge-python', 'HomebridgePythonCommand', PythonCmdAccessory);
};

function PythonCmdAccessory(log, config) {
  
  this.log = log;
  this.config = config;
  this.name = config.name;
  this.onCommand = config.on;
  this.offCommand = config.off;
  this.stateCommand = config.state;
  this.relayGpio = config.relayGpio;
  this.stateGpio = config.stateGpio;

}

PythonCmdAccessory.prototype.getServices = function() {
  
  this.informationService = new Service.AccessoryInformation();
  this.service = new Service.Switch(this.name);

  this.informationService
  .setCharacteristic(Characteristic.Manufacturer, 'Homebridge Python')
  .setCharacteristic(Characteristic.Model, 'Homebridge Plugin')
  .setCharacteristic(Characteristic.SerialNumber, '002');

  
  light = this.service.getCharacteristic(Characteristic.On)

  light.on('get', this.handleOnGet.bind(this))
  light.on('set', this.handleOnSet.bind(this));

  return [this.informationService, this.service];
};


/**
 * Handle requests to get the current value of the "On" characteristic
 */
PythonCmdAccessory.prototype.handleOnGet = function (callback){

  var accessory = this;
  var command = accessory.stateCommand+' "'+accessory.stateGpio+'"';
  var currentValue;

  exec(command, function (err, stdout, stderr) {
    if (err) {
      accessory.log('Error: ' + err);
      callback(err || new Error('Error getting state of ' + accessory.name));
    } else {
      var state = stdout.toString('utf-8').trim();
      if (state === 'ON') {
        currentValue = 1;
      }else{
        currentValue = 0;
      }
      // set this to a valid value for On
      console.log("LIGHT IS "+ state)
      callback(null, currentValue);
    }
  });



  
  // if (this.stateCommand) {
  //   console.log('stateCommand');
  // }

  
}







/**
 * Handle requests to set the "On" characteristic
 */
PythonCmdAccessory.prototype.handleOnSet = function(value, callback){
  var accessory = this;
  var command = accessory.onCommand+' "'+accessory.relayGpio+'"';
  var currentValue;

  exec(command, function (err, stdout, stderr) {
    if (err) {
      accessory.log('Error: ' + err);
      callback(err || new Error('Error getting state of ' + accessory.name));
    } else {
      var state = stdout.toString('utf-8').trim();
      if (state === 'ON') {
        currentValue = 1;
      }else{
        currentValue = 0;
      }
      // set this to a valid value for On
      console.log('Triggered SET On:' + value);
      callback(null);
    }
  });

  
}